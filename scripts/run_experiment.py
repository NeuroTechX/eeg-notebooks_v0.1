

import sys
import subprocess

def run_experiment(expt_name,subj_num = '',sess_num = '',muse_lsl_dir = 'muse-lsl'):


    lsl_record_file = '%s/lsl-record.py' % muse_lsl_dir

    if 'mlsl' in expt_name:
        expt_script_filename = expt_name.replace('mlsl_', 'generate_').replace('_test', '') + '.py'
        expt_script_file = '%s/stimulus_presentation/%s' %(muse_lsl_dir, expt_script_filename)

    if 'test' in expt_name: 
        expt_script_args = ' -d 20'
	lsl_record_args = ' -d 20'
    else:
        expt_script_args = ''
        lsl_record_args = ''
	
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

    python run_eeg_nb_experiment.py EXPT_NAME SUBJECT_NUM SESS_NUM 


    Experiment names:

    'mlsl_Visual_N170'
    'mlsl_Visual_P300'
    'mlsl_SSVEP'
    'mlsl_SSAEP'
    'mlsl_Auditory_P300'

    The muse-lsl experiments run the muse-lsl scripts with default parameters

    Add the '_test' to run a quick (20s) version


    Examples:

    python run_experiment.py mlsl_N170_test 

 
    python run_experiment.py mlsl_SSVEP




    """

    expt_name = sys.argv[1]
    
    if len(sys.argv) == 4:
       subj_num,sess_num = sys.argv[2:4]
    else:
       subj_num = ''
       sess_num = ''

    run_experiment(expt_name,subj_num,sess_num)



