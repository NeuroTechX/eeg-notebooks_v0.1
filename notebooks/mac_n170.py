from muselsl import stream, list_muses, view, record
# from multiprocessing import Process
from multiprocessing import freeze_support, set_start_method, Process, Pool
from mne import Epochs, find_events
from time import time, strftime, gmtime
import os
from stimulus_presentation import n170
from utils import utils
from collections import OrderedDict
import warnings
warnings.filterwarnings('ignore')


from optparse import OptionParser
parser = OptionParser()
 
parser.add_option("-d", "--duration",
                  dest="duration", type='int', default=400,
                  help="duration of the recording in seconds")
parser.add_option("-s", "--subject",
                  dest="subject", type='int', default=1,
                  help="subject number: must be an integer")
parser.add_option("-r", "--run",
                  dest="run", type='int', default=1,
                  help="run (session) number: must be an integer")
parser.add_option("-p", "--path",
                  dest="path", type='string', default="~/eeg-notebooks/notebooks/test.csv",
                  help="path to save recording")




#import pygame
#pygame.init()
import sys

duration = 120
subject = 2
session = 1
recording_path = '~/eeg-notebooks/notebooks/test1.csv'

stimulus = Process(target=n170.present, args=(duration,))
recording = Process(target=record, args=(duration, recording_path))

#stimulus.daemon=True
#recording.daemon=True

if __name__ == '__main__':
    #freeze_support()
    set_start_method('spawn', force=True)
    pool = Pool(processes=4)

    pool.apply_async(n170.present, args=(duration,))
    pool.apply_async(record, args=(duration,recording_path))
    
    pool.close()
    pool.join()



