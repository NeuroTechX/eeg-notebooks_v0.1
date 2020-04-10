# How to get started with eeg-notebooks: # 	

* Run the following commands in the Terminal:
```bash
cd ~
source ~/.bash_profile
conda create -n nbmac python=3
conda activate nbmac
conda install python=3.6
conda install git
git clone https://www.github.com/neurotechX/eeg-notebooks
cd ~/eeg-notebooks
pip install -r requirements_mac.txt
```
* fix pygatt code by replacing with patched version with bug commented out on lines 168-170:
```bash
cp ~/eeg-notebooks/bgapi.py ~/miniconda3/envs/nbmac/lib/python3.6/site-packages/pygatt/backends/bgapi/
```

* For the “conda create” command, you will be asked to type “y” to confirm that yes, you wish to install the required packages
* The above packages may take ~5-10 minutes to install
* Ignore the warning that muselsl is not compatible with pygatt version 3.2.0
* Run the following commands in the Terminal:
```bash
mkdir ~/.jupyter/
jupyter notebook password
```

* You will then be asked to enter a password. Leave it blank. After pressing <enter>, you will be asked to confirm your blank password
* Run the following commands in the Terminal:
```bash
python
```
```py
import matplotlib
exit()
```
```bash
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```

# Working with eeg-notebooks #

* Turn on your MUSE device 
* Connect the Bluetooth dongle to the USB port of your Mac 
* Run the following commands in the Terminal:
```bash
conda activate nbmac
cd ~/eeg-notebooks/notebooks
jupyter notebook
```

* Open mac_notebook.ipynb or cueing.ipynb in the browser
* The rest of the instructions for running experiments and analyzing data are in the mac_notebook.ipynb or cueing.ipynb notebook
