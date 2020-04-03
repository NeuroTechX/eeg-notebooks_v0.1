●	Run the following commands in the Terminal:	
		mv ~/eeg-notebooks ~/old-eeg-notebooks (if old version installed)
		source ~/.bash_profile
cd ~
		conda create -n nbmac python=3
		conda activate nbmac
conda install python=3.6
		conda install git
		git clone https://www.github.com/neurotechX/eeg-notebooks
		cd ~/eeg-notebooks
pip install -r requirements_mac.txt
●	For the “conda create” command, you will be asked to type “y” to confirm that yes, you wish to install the required packages
●	The above packages may take ~5-10 minutes to install
●	Ignore the warning that muselsl is not compatible with pygatt version 3.2.0
●	Run the following commands in the Terminal:
mkdir ~/.jupyter/
jupyter notebook password
●	You will then be asked to enter a password. Leave it blank. After pressing <enter>, you will be asked to confirm your blank password
●	Run the following commands in the Terminal:
python
import matplotlib
exit()
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc



STEP 3: Working with eeg-notebooks

●	Turn on your MUSE device 
●	Connect the Bluetooth dongle to the USB port of your Mac 
●	Run the following commands in the Terminal (in the nbmac environment)
		conda activate nbmac
cd ~/eeg-notebooks/notebooks
jupyter notebook
●	Open cueing.ipynb in the browser
●	The rest of the instructions for running experiments and analyzing data are in the cueing.ipynb notebook
