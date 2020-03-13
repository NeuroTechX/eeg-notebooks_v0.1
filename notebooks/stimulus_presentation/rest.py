import numpy as np
from pandas import DataFrame
from psychopy import visual, core, event, logging
from time import time, strftime, gmtime
from optparse import OptionParser
from pylsl import StreamInfo, StreamOutlet
from glob import glob
from random import choice
import random
import os
import scipy.io

def present(duration=300):
    nsamples = int(60*duration)
    info = StreamInfo('Markers', 'Markers', 1, 0, 'int32', 'myuidw43536')
    outlet = StreamOutlet(info)
    markernames = [1, 2]

    n_trials = 1
    screenRes = [800, 600]

    win = visual.Window(screenRes, fullscr=True, allowGUI=False, monitor='testMonitor',
                        screen=0, units='deg', name='win', color=(128,128,128), colorSpace='rgb255')
    # create fixation cross
    fCS = 60  
    fCP = [0,0] 
    fixation = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0, vertices=(
        (fCP[0]-fCS/2, fCP[1]), (fCP[0]+fCS/2, fCP[1]), (fCP[0], fCP[1]), (fCP[0], fCP[1]+fCS/2), (fCP[0], fCP[1]-fCS/2)), units='pix', closeShape=False, name='fixCross')
    fixation.autoDraw = True

    start = time()
    for i in range(nsamples):
        fixation.draw()
        #outlet.push_sample([markernames[0]], time())
        win.flip()
        #if (time() - start) > 10.0:
        #if (time() - start) > duration:
        #break
        event.clearEvents()
    print(time()-start)
    win.close()


def main():
    parser = OptionParser()
    parser.add_option("-s", "--subject",
                      dest="subject", type='string',
                      help="name of subject.")
    parser.add_option("-n", "--session",
                      dest="session", type='int',
                      help="number of session.")
    parser.add_option("-d", "--duration",
                      dest="duration", type='int', default=120,
                      help="duration of the recording in seconds.")

    (options, args) = parser.parse_args()
    present(options.subject, options.session, options.duration)


if __name__ == '__main__':
    main()
