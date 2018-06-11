from muselsl import record
from optparse import OptionParser
import sys
from time import strftime, gmtime

default_fname = ("data_%s.csv" % strftime("%Y-%m-%d-%H.%M.%S", gmtime()))

parser = OptionParser()
parser.add_option("-d", "--duration",
                  dest="duration", type='int', default=60,
                  help="duration of the recording in seconds.")
parser.add_option("-f", "--filename",
                  dest="filename", type='str', default=default_fname,
                  help="Name of the recording file.")

(options, args) = parser.parse_args()

record.record(options.duration, options.filename, True)
