

import sys
import subprocess
from optparse import OptionParser



def run_experiment(expt_name,subj_num = '',sess_num = '',muse_lsl_dir = 'muse-lsl',
		   convert_eeg_timestamps_to_localclock = '0'):


    lsl_record_file = '%s/lsl-record.py' % muse_lsl_dir

    if 'mlsl' in expt_name:
        expt_script_filename = expt_name.replace('mlsl_', 'generate_').replace('_test', '') + '.py'
        expt_script_file = '%s/stimulus_presentation/%s' %(muse_lsl_dir, expt_script_filename)


    expt_script_args = ''
    lsl_record_args = ''
    if 'test' in expt_name: 
        expt_script_args += ' -d 20'
	lsl_record_args += ' -d 20'

    lsl_record_args += ' -c ' + convert_eeg_timestamps_to_localclock


    expt_script_call = '%s %s' %(expt_script_file, expt_script_args)
    lsl_record_call = '%s %s' %(lsl_record_file, lsl_record_args)


    if sys.platform == 'win32':

       cmd = 'start python %s' %lsl_record_call
       print 'running command: \n%s' %cmd
       subprocess.call(cmd, shell=True)

       cmd =  'start python %s' %expt_script_call
       print 'running command: \n%s' %cmd 
       subprocess.call(cmd, shell=True)
       



if __name__ == '__main__':

    """
    Usage:

    python run_experiment.py [ARGS]
    
    Options: 
    
       -e EXPT_NAME 
       -c CONVERT_TIMESTAMPS 
       --subj SUBJECT_NUM 
       --sess SESS_NUM 


    Experiment names:

    'mlsl_Visual_N170'
    'mlsl_Visual_P300'
    'mlsl_SSVEP'
    'mlsl_SSAEP'
    'mlsl_Auditory_P300'

    The muse-lsl experiments run the muse-lsl scripts with default parameters

    Add the '_test' to run a quick (20s) version


    The CONVERT_TIMESTAMPS argument says whether or not to apply an internal conversion to the 
    timestamps coming from the EEG device. This should be set to '1' if using BlueMuse <= 1.0.5



    Examples:

    python run_experiment.py -e mlsl_N170_test -c 1 

 
    python run_experiment.py -e mlsl_SSVEP -c 0




    """

    parser = OptionParser()

    parser.add_option("-e", "--expt",
                      dest="expt_name", type='str', default=None,
		      help="experiment name")

    parser.add_option("--subj", "--subj_num",
                      dest="subj_num", type='str', default='',
    		      help="subject num")

    parser.add_option("--sess", "--sess_num",
                      dest="sess_num", type='str', default='',
                      help="session num")

    parser.add_option("-c", "--convert_timestamp",
                      dest="c", type='str', default='0',
		      help="convert eeg timestamp to pylsl local clock")

    (options, args) = parser.parse_args()




    run_experiment(options.expt_name,
                   options.subj_num,
		   options.sess_num, 
                   convert_eeg_timestamps_to_localclock=options.c)
    

