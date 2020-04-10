

"""
eeg-notebooks dataset fetchers
"""

import os,sys,glob



def fetch_dataset(data_dir=None, experiment=None, site='eegnb_examples', 
                  subjects='all', sessions='all', load_mne = False):

        """
        
        Return a long-form filenames list and a table saying what 
        subject and session, and run each entry corresponds to 

        Usage:
                data_dir = '/my_folder'
                experiment = 'visual-N170'
                subjects = [1]
                sessions = 'all'
                
                visn170_fnames = fetch_dataset(data_dir=data_dir, subjects='all', experiment='visual-N170',
                site='eegnb_examples')
                
                visnP300_fnames = fetch_dataset(data_dir=data_dir, subjects=[1], experiment='visual-P300',
                site='eegnb_examples')
                


        """;
        
        
    
        experiments_list = ['rest', 'auditory-P300', 'auditory-SSAEP', 'visual-cueing',
                          'visual-gonogo','visual-leftright','visual-N170',
                          'visual-P300','visual-spatialfreq', 'visual-SSVEP']
        
        gdrive_locs = {'visual-SSVEP':'1zj9Wx-YEMJo7GugUUu7Sshcybfsr-Fze',
                        'visual-spatialfreq':'1ggBt7CNvMgddxji-FvxcZoP-IF-PmESX',
                        'visual-P300':'1OLcj-zSjqdNrsBSUAsGBXOwWDnGWTVFC',
                        'visual-N170': '1oStfxzEqf36R5d-2Auyw4DLnPj9E_FAH',
                        'visual-leftright': '1f8A4Vbz0xjfgGIYFldMZ7ZL02x7T0jSt',
                        'visual-nogono': '1C8WKg9TXyp8A3QJ6T8zbGnk6jFcMutad',
                        'auditory-SSAEP': '1fd0OAyNGWWOHD8e1FnEOLeQMeEoxqEpO',
                        'auditory-P300': '1OEtrRfMOkzDssGv-2Lj56FsArmPnQ2vD'}
        
        wget_str_tpl = "wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=%s' -O %s"



        if experiment not in experiments_list: raise ValueError('experiment not in database')


        download_it = False
        exp_dir = os.path.join(data_dir, experiment, site)
        
        if not os.path.isdir(exp_dir): download_it = True

        if download_it:
            cwd = os.getcwd()
            code = gdrive_locs[experiment]
            outfile = '%s/%s' %(data_dir, experiment + '.zip')
            wget_str = wget_str_tpl %(code,outfile)
            
            print('downloading zip file: for %s' %experiment)
            print(wget_str)
            os.system(wget_str)
            
            os.chdir(data_dir)
            os.system('unzip %s' %outfile)
            
            os.chdir(cwd)
            
           
        
        if subjects == 'all': subjects = ['*']
        if sessions == 'all':  sessions = ['*']
            
        fnames = []
        for subject_nb in subjects:
            for session_nb in sessions:
                pth = '{}/subject{}/session{}/*.csv'.format(exp_dir,subject_nb, session_nb)
                fpaths = glob.glob(pth)
                fnames += fpaths

                
            
        return fnames

