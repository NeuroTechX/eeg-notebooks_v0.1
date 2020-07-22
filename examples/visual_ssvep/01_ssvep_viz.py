"""
SSVEP Visualization
===============================

This notebook runs only the data analysis part of N170 notebook.

Look at the notes to see how this can be run on the web with binder or google collab.

All of the additional notes are removed; only the code cells are kept.

"""

###################################################################################################

# Imports
from muselsl import stream, list_muses, view, record
from multiprocessing import Process
from mne import Epochs, find_events
from time import time, strftime, gmtime
import os
#from stimulus_presentation import n170
#from eegnb.experiments.visual_n170 import n170
from eegnb.datasets import datasets
from eegnb.analysis import utils
from collections import OrderedDict
import warnings
warnings.filterwarnings('ignore')

# sphinx_gallery_thumbnail_number = 2

###################################################################################################
# Skipping these steps                                                                                                  # ---------------------
#
# Step 1: Connect to an EEG Device
# Step 2: Apply the EEG Device and Wait for Signal Quality to Stabilize
# Step 3: Run the Experiment

###################################################################################################
# Load Data
# ---------------------
#
# We will use the
# `MNE sample dataset <https://mne.tools/stable/overview/datasets_index.html?#sample>`_
# which is a combined MEG/EEG recording with an audiovisual task.
#
# First we will load the dataset from MNE, have a quick look at the data,
# and extract the EEG data that we will use for this example.
#
# Note that if you are running this locally, the following cell will download
# the example dataset, if you do not already have it.
#

###################################################################################################

eegnb_data_path = os.path.join(os.path.expanduser('~/'),'.eegnb', 'data')    
ssvep_data_path = os.path.join(eegnb_data_path, 'visual-SSVEP', 'eegnb_examples')

# If dataset hasn't been downloaded yet, download it 
if not os.path.isdir(ssvep_data_path):
  datasets.fetch_dataset(data_dir=eegnb_data_path, experiment='visual-SSVEP', site='eegnb_examples')        


subject = 1
session = 1

raw = utils.load_data(ssvep_data_path, sfreq=256., 
                      subject_nb=subject, session_nb=session,
                      ch_ind=[0, 1, 2, 3, 4], 
                      replace_ch_names={'Right AUX': 'POz'})


###################################################################################################
# Visualize the power spectrum
# ----------------------------

#%matplotlib inline
raw.plot_psd()

###################################################################################################
# Epoching
# ----------------------------

# Next, we will chunk (epoch) the data into segments representing the data 100ms before to 800ms after each stimulus.

# Note: we will not reject epochs here because the amplitude of the SSVEP at POz is so large it is difficult to separate from eye blinks

events = find_events(raw)
event_id = {'30 Hz': 1, '20 Hz': 2}
epochs = Epochs(raw, events=events, event_id=event_id, 
                            tmin=-0.5, tmax=4, baseline=None, preload=True,
                                            verbose=False, picks=[0, 1, 2, 3, 4])
print('sample drop %: ', (1 - len(epochs.events)/len(events)) * 100)




####################################################################################################
# Stimuli-Specific PSD
# ----------------------

# Next, we can compare the PSD of epochs specifically during 20hz and 30hz stimulus presentation

#%matplotlib inline
from matplotlib import pyplot as plt
from mne.time_frequency import psd_welch
import numpy as np



f, axs = plt.subplots(2, 1, figsize=(10, 10))
psd1, freq1 = psd_welch(epochs['30 Hz'], n_fft=1028, n_per_seg=256 * 3)
psd2, freq2 = psd_welch(epochs['20 Hz'], n_fft=1028, n_per_seg=256 * 3)
psd1 = 10 * np.log10(psd1)
psd2 = 10 * np.log10(psd2)

psd1_mean = psd1.mean(0)
psd1_std = psd1.mean(0)


psd2_mean = psd2.mean(0)
psd2_std = psd2.mean(0)


axs[0].plot(freq1, psd1_mean[[0, 3], :].mean(0), color='b', label='30 Hz')

axs[0].plot(freq2, psd2_mean[[0, 3], :].mean(0), color='r', label='20 Hz')


axs[1].plot(freq1, psd1_mean[4, :], color='b', label='30 Hz')

axs[1].plot(freq2, psd2_mean[4, :], color='r', label='20 Hz')


axs[0].set_title('TP9 and TP10')

axs[1].set_title('POz')

axs[0].set_ylabel('Power Spectral Density (dB)')

axs[1].set_ylabel('Power Spectral Density (dB)')

axs[0].set_xlim((2, 50))

axs[1].set_xlim((2, 50))

axs[1].set_xlabel('Frequency (Hz)')

axs[0].legend()

axs[1].legend()


plt.show();

# With this visualization we can clearly see distinct peaks at 30hz and 20hz in the PSD, corresponding to the frequency of the visual stimulation. The peaks are much larger at the POz electrode, but still visible at TP9 and TP10


####################################################################################################
# Spectrogram
# -----------

# We can also look for SSVEPs in the spectrogram, which uses color to represent the power of frequencies in the EEG signal over time

from mne.time_frequency import tfr_morlet

frequencies = np.logspace(1, 1.75, 60)
tfr, itc = tfr_morlet(epochs['30 Hz'], freqs=frequencies, 
                              n_cycles=15, return_itc=True)
tfr.plot(picks=[4], baseline=(-0.5, -0.1), mode='logratio', 
                 title='POz - 30 Hz stim');

tfr, itc = tfr_morlet(epochs['20 Hz'], freqs=frequencies, 
                              n_cycles=15, return_itc=True)
tfr.plot(picks=[4], baseline=(-0.5, -0.1), mode='logratio', 
                 title='POz - 20 Hz stim');

plt.tight_layout()

# Once again we can see clear SSVEPs at 30hz and 20hz

 
# We can use a filter bank approach on the original 4 Muse electrodes (to see how the headband alone without external electrodes could be used to classify SSVEP):

#    - Apply bandpass filters around both stimulation frequencies
#    - Concatenate bandpass-filtered channels
#    - Extract epochs (from 1 to 3 s after stimulus onset, to avoid classifying the ERP)
#    - Apply common classification pipelines

# Bandpass filter the raw data
muse_raw = raw.drop_channels(['POz'])
raw_filt_30Hz = muse_raw.copy().filter(25, 35, method='iir')
raw_filt_20Hz = muse_raw.copy().filter(15, 25, method='iir')
raw_filt_30Hz.rename_channels(lambda x: x + '_30Hz')
raw_filt_20Hz.rename_channels(lambda x: x + '_20Hz')

# Concatenate with the bandpass filtered channels
raw_all = raw_filt_30Hz.add_channels([raw_filt_20Hz], 
                                            force_update_info=True)

# Extract epochs
events = find_events(raw_all)
event_id = {'30 Hz': 1, '20 Hz': 2}

epochs_all = Epochs(raw_all, events=events, event_id=event_id, tmin=1, 
                             tmax=3, baseline=None, reject={'eeg': 100e-6}, 
                                                  preload=True, verbose=False,)

epochs_all.pick_types(eeg=True)
X = epochs_all.get_data() * 1e6
times = epochs.times
y = epochs_all.events[:, -1]





