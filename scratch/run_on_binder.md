
# Run eeg-notebooks on binder

You can run all of the post-data acquisition analyses in the muse-lsl and eeg-notebooks 
jupyter notebooks without any local installations, in the cloud, completely free, using the wonderful binder. 

This process can certainly be streamlined, but currently the following is sufficient and quick:

I (pseudo)-randomly selected [this repository](https://github.com/jvns/pandas-cookbook) to use as the starting point,
because it already has pandas and matplotlib installed. Others could be used instead; doesn't really matter.

You need to do the following:


- Navigate to [this repository](https://mybinder.org/v2/gh/jvns/pandas-cookbook/master) in a browser
- Open up a terminal and type `pip install seaborn mne scikit-learn pyriemann`
- Open up a second terminal and type `git clone https://github.com/neurotechx/eeg-notebooks`
- Open up a notebook and (when the above two have completed), navigate to `eeg-notebooks/notebooks`
- I've verified the following notebooks work with this instruction set:



