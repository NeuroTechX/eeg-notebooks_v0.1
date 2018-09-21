# EEG Notebooks

A collection of classic EEG experiments implemented in Python and Jupyter notebooks. This repo is a work in progress with the goal of making it easy to perform classical EEG experiments and automatically analyze data.

Currently, all experiments are implemented for the Muse EEG device and based on work done by Alexandre Barachant and Hubert Banville for the [muse-lsl](https://github.com/alexandrebarachant/muse-lsl) library. 

Please see the [documentation](http://eeg-notebooks.readthedocs.io/) for advanced installation instructions and complete info about the project.

## Getting Started

Follow installation instructions [here](http://eeg-notebooks.readthedocs.io/en/latest/setup_instructions_windows.html)

If you are a Mac user, follow the installation instructions [here](https://github.com/amandakeasson/eeg-notebooks/blob/master/mac_instructions.pdf)

## Running Experiments

Open the experiment you are interested in running in notebooks folder. Notebooks can be opened either with the Jupyter Notebook browser environment (run `jupyter notebook`) or in the [nteract](https://nteract.io/desktop) desktop application.

All experiments should be able to performed entirely within the notebook environment. On Windows 10, you will want to skip the bluetooth connection step and start an EEG data stream through the [BlueMuse](https://github.com/kowalej/BlueMuse) GUI.

*Note: if errors are encountered during viewing of the eeg data, try starting the viewer directly from the command line (`muselsl view`). Version 2 of the viewer may work better on Windows computers (`muselsl view -v 2`)

Currently available experiments: 
- N170 (Faces & Houses)
- SSVEP
- Visual P300

