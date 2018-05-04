


PYTHON_EXE=$HOME/Miniconda2/python.exe
EEG_NB_DIR=$HOME/GitBash/eeg-notebooks
MUSE_LSL_DIR=$EEG_NB_DIR/muse-lsl

cd $MUSE_LSL_DIR

start winpty $PYTHON_EXE $MUSE_LSL_DIR/stimulus_presentation/generate_SSVEP.py 

start winpty $PYTHON_EXE $MUSE_LSL_DIR/lsl-record.py


