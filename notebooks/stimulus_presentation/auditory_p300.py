"""
Generate Auditory P300
======================

Auditory oddball paradigm stimulus presentation.

"""
from time import time
from optparse import OptionParser

import numpy as np
from pandas import DataFrame
from psychopy import visual, core, event, sound
from pylsl import StreamInfo, StreamOutlet

def present(duration=120):
    

    # Create markers stream outlet
    info = StreamInfo('Markers', 'Markers', 1, 0, 'int32', 'myuidw43536')
    outlet = StreamOutlet(info)

    markernames = [1, 2]
    start = time()

    # Set up trial parameters
    n_trials = 2010
    iti = 0.3
    soa = 0.2
    jitter = 0.2
    record_duration = np.float32(duration)

    # Initialize stimuli
    aud1 = sound.Sound('C', octave=5, sampleRate=44100, secs=0.2)
    aud1.setVolume(0.8)
    aud2 = sound.Sound('D', octave=6, sampleRate=44100, secs=0.2)
    aud2.setVolume(0.8)
    auds = [aud1, aud2]

    # Setup trial list
    sound_ind = np.random.binomial(1, 0.25, n_trials)
    trials = DataFrame(dict(sound_ind=sound_ind, timestamp=np.zeros(n_trials)))

    # Setup graphics
    mywin = visual.Window([1920, 1080], monitor='testMonitor', units='deg',
                          fullscr=True)
    fixation = visual.GratingStim(win=mywin, size=0.2, pos=[0, 0], sf=0,
                                  rgb=[1, 0, 0])
    fixation.setAutoDraw(True)
    mywin.flip()

    for ii, trial in trials.iterrows():
        # Intertrial interval
        core.wait(iti + np.random.rand() * jitter)

        # Select and play sound
        ind = trials['sound_ind'].iloc[ii]
        auds[ind].stop()
        auds[ind].play()

        # Send marker
        timestamp = time()
        outlet.push_sample([markernames[ind]], timestamp)

        # offset
        core.wait(soa)
        if len(event.getKeys()) > 0 or (time() - start) > record_duration:
            break
        event.clearEvents()

    # Cleanup
    mywin.close()


def main():
    parser = OptionParser()

    parser.add_option("-d", "--duration",
                      dest="duration", type='int', default=120,
                      help="duration of the recording in seconds.")

    (options, args) = parser.parse_args()
    present(options.duration)


if __name__ == '__main__':
    main()
