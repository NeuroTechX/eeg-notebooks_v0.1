
# Muse-lsl on Windows

Notes on acquiring and analyzing data using muse-lsl on windows.


## Environment

The environment setup we are aiming for is minimal possible: anaconda/miniconda windows installation, and then using the windows anaconda prompt. 

An alternative, which I personally prefer, is to use windows git bash terminals. This is preferable for me simply because the linux terminal is a more familiar development. 

The program calls and script contents are listed in full below. In a nutshell: we use 'start' to spawn new concurrent python processes (in new windows terminals)


Anaconda shell: 

- use a .bat script
- e.g. 'start python (script name)'


Git bash: 

- use a .sh script
- need to tell it where the anaconda python installation is. use winpty for that. 
- e.g. 'start winpty (path-to-anaconda)/python.exe (script name)'




## Connection

In order to use muse-lsl on windows, you need to have a BLED112 bluetooth dongle. 


The muse-lsl script doesn't appear to be able to be able to connect to the dongle automatically every time. 

Inserting the dongle and then restarting windows appears to solve this problem. 

Supplying the muse device's IP address doesn't appear to solve it. 


## Running scripts

In order to acquire data for the psychopy experiments, it is necessary to have three python processes running concurrently:

`python muse-lsl.py`  
`python (stim presentation script)`  
`python lsl-record.py`  


You can't use the linux bash ampersand (&) to chain commands in the windows shell; need to put the commands in a script (as noted above). 


Here are some minimal script contents to get going:



Git bash script contents:


`start winpty /c/Users/John/Miniconda2/python.exe /c/Users/John/GitBash/muse-lsl/stimulus_presentation/generate_SSVEP.py -d 10`  
`start winpty /c/Users/John/Miniconda2/python.exe /c/Users/John/GitBash/muse-lsl//lsl-record.py -d 10`  


Run with:

`bash jg_record_SSVEP.sh`  



Anaconda prompt script contents:


`start python C:\Users\John\GitBash\muse-lsl\stimulus_presentation\generate_SSVEP.py -d 10`    
`start python C:\Users\John\GitBash\muse-lsl\lsl-record.py -d 10`  


Run with:

`jg_record_SSVEP.bat`  

















