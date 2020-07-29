===================================================================
EEG-Notebooks - Democratizing the cognitive neuroscience experiment
===================================================================

.. image:: https://github.com/NeuroTechX/eeg-notebooks/raw/thebigrefactor/doc/img/eeg-notebooks_logo.png
   :width: 600
   :align: center

EEG-Notebooks is a collection of classic EEG experiments, implemented in Python and Jupyter notebooks. The experimental protocols and analyses are quite generic, but are primarily taylored for low-budget / consumer EEG hardware such as the InteraXon MUSE and OpenBCI Cyton. The goal is to make cognitive neuroscience and neurotechnology more accessible, affordable, and scalable - democratizing the cognitive neuroscience experiment. 


Overview
--------

Conventional lab-based EEG research typically uses research-grade (often high-density) EEG devices, dedicated stimulus delivery software and hardware, and dedicated technicians responsible for operating this equipment. The price tag for these items can easily extend into hundreds of thousands of dollars, which naturally places major limits on their acquisition and usage. 

In recent years, however, developments in hardware and software technologies are making it possible for many classic EEG cognitive neuroscience experiments to be conducted using a standard laptop/personal computer and a relatively cheap (<$1000) consumer-grade EEG device, with a combined cost of less than 1000 dollars. This opens dramatic new possibilities for neurotechnology and cognitive neuroscience education at both the high school and university levels, as well as more ambitious and larger-scale research and clinical applications. We like to think of this as representing the *democratization of the cognitive neuroscience experiment*.

The aim of the EEG-Notebooks project is to provide the critical 'glue' that pulls together the various enabling technologies necessary for running and analyzing EEG-based cognitive neuroscience experiments. These include: 

- streaming data from various relatively new wireless consumer-grade EEG devices  
- visual and auditory stimulus presentation, concurrent with and time-locked to EEG recordings  
- a growing library of well-documented, ready-to-use, and ready-to-modify experimental designs  
- relevant signal processing, statitical and machine learning analysis functionalities


Documentation
-------------

Documentation for eeg-notebooks is available on the
`documentation site <https://neurotechx.github.io/eeg_notebooks/index.html>`_.


Installation
------------

The current version of eeg-noteboks is the 0.2.X series. The code-base and API are under major development and subject to change. 

Check the `changelog <https://neurotechx.github.io/eeg-notebooks/changelog.html>`_ for notes on changes from previous versions. 


**Development Version**

To get the current development version, first clone this repository:

.. code-block:: shell

    $ git clone https://neurotechx/eeg-notebooks

To install this cloned copy, move into the directory you just cloned, and run:

.. code-block:: shell

    $ pip install .

**Editable Version**

To install an editable version, download the development version as above, and run:

.. code-block:: shell

    $ pip install -e .



Quickstart
----------



.. code-block:: python

    $ #
    $ # Imports
    $ import os
    $ from eegnb import generate_save_fn
    $ from eegnb.devices.eeg import EEG
    $ from eegnb.experiments.visual_n170 import n170
    $ from eegnb.analysis import load_data
    $ #
    $ # Define some variables
    $ board_name = 'muse'
    $ experiment = 'visual_n170'
    $ subject = 'test'
    $ record_duration=120
    $ # 
    $ # Initiate EEG device 
    $ eeg_device = EEG(device=board_name)
    $ #
    $ # Create output filename
    $ save_fn = generate_save_fn(board_name, experiment, subject)
    $ #
    $ # Run experiment
    $ n170.present(duration=record_duration, eeg=eeg_device, save_fn=save_fn)
    $ #
    $ # Load recorded data
    $ raw = load_data(save_fn)
    $ #

Acknowledgments
----------------

EEG-Notebooks was created by the `NeurotechX <https://neurotechx.com/>`_ hacker/developer/neuroscience community. The ininitial idea and majority of the groundwork was due to Alexandre Barachant - including the `muse-lsl <https://github.com/alexandrebarachant/muse-lsl/>`_ library, which is core dependency. Lead developer on the project is now `John Griffiths <www.grifflab.com>`_ . 

Key contributors include: Alexandre Barachant, Hubert Banville , Dano Morrison, Ben Shapiro, John Griffiths, Amanda Easson, Kyle Mathewson, Jadin Tredup. 


Contribute
----------

This project welcomes and encourages contributions from the community!

If you have an idea of something to add to eeg-notebooks, please start by opening an
`issue <https://github.com/neurotechx/eeg-notebooks/issues>`_.


Bug reports
-----------

Please use the `Github issue tracker <https://github.com/neurotechx/eeg-notebooks/issues>`_
to file bug reports and/or ask questions about this project.


