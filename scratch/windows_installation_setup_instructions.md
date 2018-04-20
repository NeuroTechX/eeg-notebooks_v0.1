
# muse-lsl + eeg-notebooks windows installation + setup instructions


## a) Install miniconda

Miniconda is a 'mini' version of the anaconda python distribution. 

- Download + run the windows miniconda installer from [here](https://conda.io/miniconda.html) (python 2.7 version)

- Start an anaconda terminal (good idea = add shortcut to windows toolbar)

- Type `pip install bitstring pylsl pygatt psychopy scikit-learn pandas numpy mne seaborn pexpect jupyter`
- Type `jupyter notebook password` , and enter a password of your choice. That you will remember. You will use this every time you start a jupyter notebook. 

## b) (Optional) Download git bash for windows

Git bash gives you a linux-style terminal, as well as a git installation and a few other useful linuxy things.


## c) Get eeg-notebooks

With git bash: 

`git clone https://github.com/NeuroTechX/eeg-notebooks`

Without git bash:

Navigate to the [github repository](https://github.com/NeuroTechX/eeg-notebooks) in a web browser and download. 

---

You should now be able to do the following:


- Start an anaconda terminal (good idea = add shortcut to windows toolbar)
- Go to the `eeg-notebooks` folder you have created
- Type `jupyter notebook --no-browser`
- In a web browser: `localhost:8888`. This should bring up the `eeg-notebooks` folder structure. 
- Go to the `notebooks` folder, open up one of the notebooks, and work through the cells.


## d) Connect to the muse device

*to add*




---

TO DO FOR THESE INSTRUCTIONS: 


- Fool proof for complete newbies. Add pictures. 
- Don't assume knowledge of directory navigation in terminals etc. 
- Create a tests function in eeg-notebooks, to be run as final step in these instructions. 
- Package versions for `pip install`
- Correct `pygatt` version. Needs to be 1.2 ?
- Move git bash option to end so it isn't confusing / daunting
- All mMuse hardward







