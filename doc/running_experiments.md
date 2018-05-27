
# Running experiments

All of the original `muse-lsl` and new `neurobrite` cognitive experiments can be run from `eeg-notebooks` using a call to [scripts/run_experiment.py](https://github.com/NeuroTechX/eeg-notebooks/blob/master/scripts/run_experiment.py)

As explained in the `run_experiment.py' docstring, calls to this function are done with the following:

```python
python scripts/run_experiment.py EXPT_NAME SUBJECT_NUM SESS_NUM 
```

*Experiment names:*

'mlsl_Visual_N170'  

'mlsl_Visual_P300'  

'mlsl_SSVEP'   

'mlsl_SSAEP'  

'mlsl_Auditory_P300'  


The muse-lsl experiments run the muse-lsl scripts with default parameters
Add the '_test' to run a quick (20s) version


*Examples:*

```python
python scripts/run_experiment.py mlsl_N170_test 
 
python scripts/run_experiment.py mlsl_SSVEP
```



