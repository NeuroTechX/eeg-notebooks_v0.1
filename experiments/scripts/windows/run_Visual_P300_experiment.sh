
PYTHON_EXE=$HOME/Miniconda2/python.exe
EEG_NB_DIR=$HOME/GitBash/eeg-notebooks


start winpty $PYTHON_EXE $EEG_NB_DIR/stimulus_presentation/generate_Visual_P300.py 

start winpty $PYTHON_EXE $EEG_NB_DIR/lsl-record.py


