
# Running experiments

All of the original `muse-lsl` and new `neurobrite` cognitive experiments can be run from `eeg-notebooks` using a call to [scripts/run_experiment.py](https://github.com/NeuroTechX/eeg-notebooks/blob/master/scripts/run_experiment.py)

As explained in the `run_experiment.py' docstring, calls to this function are done with the following:

```python
python scripts/run_experiment.py -e EXPT_NAME -c BMW_FLAG
```

*Experiment names:*

'mlsl_Visual_N170'  

'mlsl_Visual_P300'  

'mlsl_SSVEP'   

'mlsl_SSAEP'  

'mlsl_Auditory_P300'  


The muse-lsl experiments run the muse-lsl scripts with default parameters

Add the '_test' to run a quick (20s) version

`BMW_FLAG` indicates whether you are using BlueMuse on windows for the EEG bluetooth connection. If so, this needs to be `-c 1`. Otherwise, `-c 0` (or omit; as this is the default). 


*Examples:*

```python
python scripts/run_experiment.py -e mlsl_N170_test -c 1 
 
python scripts/run_experiment.py -e mlsl_SSVEP
```



