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

#import pygame
#pygame.init()
import sys

recording_path = '~/codeOther/eeg-notebooks/notebooks/test.csv'

duration = 30
subject = 1
session = 1

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



