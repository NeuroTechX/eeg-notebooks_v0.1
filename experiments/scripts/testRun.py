import sys
import os

sys.path.append(os.path.join(os.curdir, "stimulus_presentation"))

from generate_Auditory_P300 import generate_Auditory_P300

generate_Auditory_P300(10)