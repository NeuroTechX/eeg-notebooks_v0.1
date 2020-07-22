"""
N170 Classification
===============================

Classification 

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
n170_data_path = os.path.join(eegnb_data_path, 'visual-N170', 'eegnb_examples')

# If dataset hasn't been downloaded yet, download it 
if not os.path.isdir(n170_data_path):
  datasets.fetch_dataset(data_dir=eegnb_data_path, experiment='visual-N170', site='eegnb_examples')        


subject = 1
session = 1

raw = utils.load_data(n170_data_path, sfreq=256., 
                              subject_nb=subject, session_nb=session)

###################################################################################################
# Visualize the power spectrum
# ----------------------------

#%matplotlib inline
#raw.plot_psd()

###################################################################################################
# Filteriing
# ----------------------------

raw.filter(1,30, method='iir')
#raw.plot_psd(fmin=1, fmax=30);

###################################################################################################
# Epoching
# ----------------------------

# Create an array containing the timestamps and type of each stimulus (i.e. face or house)
events = find_events(raw)
event_id = {'House': 1, 'Face': 2}

# Create an MNE Epochs object representing all the epochs around stimulus presentation
epochs = Epochs(raw, events=events, event_id=event_id, 
                        tmin=-0.1, tmax=0.8, baseline=None,
                                        reject={'eeg': 75e-6}, preload=True, 
                                                        verbose=False, picks=[0,1,2,3])
print('sample drop %: ', (1 - len(epochs.events)/len(events)) * 100)
epochs

###################################################################################################
# Epoch average
# ----------------------------

#%matplotlib inline
conditions = OrderedDict()
conditions['House'] = [1]
conditions['Face'] = [2]

###################################################################################################
# Conclusions
# ----------------------------

# Blah

import pandas as pd
from sklearn.pipeline import make_pipeline

from mne.decoding import Vectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit

from pyriemann.estimation import ERPCovariances, XdawnCovariances
from pyriemann.tangentspace import TangentSpace
from pyriemann.classification import MDM

from collections import OrderedDict

clfs = OrderedDict()

clfs['Vect + LR'] = make_pipeline(Vectorizer(), StandardScaler(), LogisticRegression())
clfs['Vect + RegLDA'] = make_pipeline(Vectorizer(), LDA(shrinkage='auto', solver='eigen'))
clfs['ERPCov + TS'] = make_pipeline(ERPCovariances(estimator='oas'), TangentSpace(), LogisticRegression())
clfs['ERPCov + MDM'] = make_pipeline(ERPCovariances(estimator='oas'), MDM())
clfs['XdawnCov + TS'] = make_pipeline(XdawnCovariances(estimator='oas'), TangentSpace(), LogisticRegression())
clfs['XdawnCov + MDM'] = make_pipeline(XdawnCovariances(estimator='oas'), MDM())

# format data
epochs.pick_types(eeg=True)
X = epochs.get_data() * 1e6
times = epochs.times
y = epochs.events[:, -1]

# define cross validation 
cv = StratifiedShuffleSplit(n_splits=20, test_size=0.25, 
                                    random_state=42)

# run cross validation for each pipeline
auc = []
methods = []
for m in clfs:
    print(m)
    try:
        res = cross_val_score(clfs[m], X, y==2, scoring='roc_auc', 
                              cv=cv, n_jobs=-1)
        auc.extend(res)
        methods.extend([m]*len(res))
    except:
        pass




## Plot Decoding Results

import seaborn as sns
from matplotlib import pyplot as plt

    
results = pd.DataFrame(data=auc, columns=['AUC'])
results['Method'] = methods

fig = plt.figure(figsize=[8,4])
sns.barplot(data=results, x='AUC', y='Method')
plt.xlim(0.4, 0.9)
sns.despine()


