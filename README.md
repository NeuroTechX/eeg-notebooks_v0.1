# EEG Notebooks

A collection of classic EEG experiments implemented in Python and Jupyter notebooks. This repo is a work in progress with the goal of making it easy to perform classical EEG experiments and automatically analyze data.

Currently, all experiments are implemented for the Muse EEG device and based on work done by Alexandre Barachant and Hubert Banville for the [muse-lsl](https://github.com/alexandrebarachant/muse-lsl) library

## Getting Started

You will need a Muse 2016 and Python installed on your computer. With the exception of some of the stimulus presentation scripts, all code will work with Python 3.

The muse-lsl library that manages connecting to Muse and recording data is incorporated into this repo as a submodule. In order to get it up and running use the following commands:


Either: 

```
git clone --recursive https://github.com/neurotechx/eeg-notebooks
```


Or: 

```
git clone https://github.com/neurotechx/eeg-notebooks
cd eeg-notebooks
git submodule init
git submodule update
```

Install all requirements

`pip install requirements.txt`

To connect to your Muse and begin streaming data

`python muse-lsl/muse-lsl.py --name MUSE_YOURDEVICEID`

IMPORTANT: Leave this terminal running while you are recording data performing experiments

To visualize streaming data 

`python muse-lsl/lsl-viewer.py`

IMPORTANT: If you intend to collect data for an experiment, ensure that your signal quality is "excellent" and that there is very little noise before proceeding.

### Running an experiment

With the muse-lsl.py script running, open another terminal and run

`python stimulus_presentation/PARADIGM.py -d 120 & python muse-lsl/lsl-record.py -d 12`

where `PARADIGM.py` is one of the stimulus presentation scripts described above (e.g., `generate_Visual_P300.py`).

This will launch the selected paradigm and record data for 2 minutes. Consider repeating this 6 - 10 times in order to gather enough data.

After collecting data, move your recorded data CSVs to the data folder. Currently, notebook analysis scripts work with a `experiment/type/subjectNumber/sessionNumber` directory structure.

Open the Jupyter notebook relevant to the experiment your performed (e.g. `P300 with Muse.ipynb`) to analyze your data

## Available Notebooks

### [Visual P300 with Oddball paradigm](https://github.com/NeuroTechX/eeg-notebooks/blob/master/notebooks/P300%20with%20Muse.ipynb)
The visual P300 is a spike that occurs 300ms after perceiving a visual stimulus that has implications on decision making. This was validated in Muse by Alexandre Barachant with the Oddball paradigm, in which low-probability target items (oddballs) are interspersed with high probability non-target items. With AB's paradigm, the experiment takes about 10 minutes to run (5 x 2 minute trials). Although the Muse's sensors aren't in the ideal position for detecting the P300, AB was able to attan "good" accuracy in identifying P300 spikes.

### [Auditory P300](https://github.com/NeuroTechX/eeg-notebooks/blob/master/notebooks/Auditory%20P300%20with%20Muse.ipynb)
Same as the visual P300, but dependent on auditory stimulus. Auditory P300s are normally less distinguishable than visual P300s, but they may be more suited to the Muse since its electrodes are closer to auditory centers (superior temporal cortex).

### [C1 and P1](https://github.com/NeuroTechX/eeg-notebooks/blob/master/notebooks/Left-Right%20visual%20field%20with%20Muse.ipynb)
C1 and P1 are two ERPs related to the perception of a visual stimulus. The C1 is the first component, appearing in the 65-90ms range after stimulus onset while the P1 appears later, around 100ms.

C1 and P1 were validated in Muse by Hubert with a left/right visual field experiment. Comparing ERPs to left or right-field presentation of visual stimuli revealed a contralateral pattern of C1 and P1 in the both the temporal and anterior electrodes. However, their timing seems a little delayed

### [N170](https://github.com/NeuroTechX/eeg-notebooks/blob/master/notebooks/N170%20with%20Muse.ipynb)
The N170 is an ERP specifically related to the perception of faces. This was validated in Muse by Hubert with a 12 minute experiment (6 x 2 minute trials). Stimuli consists of 12 pictures of houses and 12 pictures of faces. Accuracy of N170 detection is rather good.

### [SSAEP](https://github.com/NeuroTechX/eeg-notebooks/blob/master/notebooks/SSAEP%20with%20Muse.ipynb)
The steady state auditory evoked potential is a frequency response produced when hearing modulating tones of certain frequencies. It was validated in Muse by Hubert, who used 45hz and 40hz amplitude modulation applied to 900 and 770h carrier frequencies. A PSD of the produced EEG signal showed clear spikes, correspondingly, at 45 and 40hz in the temporal electrodes. The N100 and P200 complex was also noticed at the beginning of stimulus onset 

### [SSVEP](https://github.com/NeuroTechX/eeg-notebooks/blob/master/notebooks/SSVEP%20with%20Muse.ipynb)
The steady state visual evoked potential is a frequency response produced visual stimulation at specific frequencies. It was validated by Hubert in a 12 minute experiment (6 x 2 minute trials). Stimulation frequencies of 30hz and 20hz were used and an extra electrode at POz was added. Found clear peaks in the PSD at the stimulation frequencies. The peaks were most significant at the extra electrode, which is closest to the primary visual regions, but was detectable at all electrodes and found to have remarkably high accuracy when using a filter bank approach to isolate specific frequencies. 


## Unvalidated Experiments and other phenomena

### N100 - P200
The combination of a negative evoked potential around 100ms after any unpredictable stimulus and a positive potential 200ms after. These were noticed in Hubert's SSAEP experiment, but not independently classified or tested.

### On-task Beta
Noticed in Hubert's visual grating test, but difficult to extract.

### Alpha reset
A noticeable increase in alpha activity after stimulus presentation ends. Noticed in Hubert's visual grating test.

## Details related to Muse ERP analysis

- Latency and jitter related from the Muse is [40ms +-20ms](https://www.frontiersin.org/articles/10.3389/fnins.2017.00109/full)  
- In Krigolson lab's resampling analysis, a sample size of 10 was found to be needed for high statistical accuracy for N200 and reward positivity, which is similar to traditional EEG, but greater numbers of subjects were needed for P300
