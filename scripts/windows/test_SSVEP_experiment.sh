


PYTHON_EXE=$HOME/Miniconda2/python.exe
EEG_NB_DIR=$HOME/GitBash/eeg-notebooks
MUSELSL_DIR=$EEG_NB_DIR/muse-lsl

rm $EEG_NB_DIR/data/test/SSVEP_test_report.txt

start winpty $PYTHON_EXE $MUSELSL_DIR/stimulus_presentation/generate_SSVEP.py -d 30 

winpty $PYTHON_EXE $MUSELSL_DIR/lsl-record.py -d 30 -f "$EEG_NB_DIR/data/test/SSVEP_test.csv" 

winpty $PYTHON_EXE $EEG_NB_DIR/scripts/windows/check_impedance.py $EEG_NB_DIR/data/test/SSVEP_test.csv SSVEP 

echo "impedances check report in SSVEP_test_report.txt"

echo `cat SSVEP_test_report.txt`



