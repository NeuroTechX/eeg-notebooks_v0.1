import scipy.io as sio 
import os

subs = [101, 102]
subs = [101]

n_subs = len(subs)
n_sesh = 1#2
n_cond = 2
conditions = ['valid','invalid']

rt_toofast = 250
rt_tooslow = 1500

#creates arrays to save output

for sub in subs:

	print('Subject - ' + str(sub))

	for sesh in range(n_sesh):
		print('Session - ' + str(sesh+1))
		path =  './subject' + str(sub) + '/session' + str(sesh+1) + '/'
		file =  [x for x in os.listdir(path) if x.endswith('.mat')]
		output_dict = sio.loadmat(path + file[0])

		print(output_dict['output'].shape)
		print(output_dict['column_labels'])

		output = output_dict['output']
		accuracy = output[:,6]
		rt = output[:,7]
		validity = output[:,3]

		#populate the output


print('Done')
