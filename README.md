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



(See [here](http://eeg-notebooks.readthedocs.io/en/latest/setup_instructions_windows.html)


for more detailed setup instructions for windows operating systems)



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

