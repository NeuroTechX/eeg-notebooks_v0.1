import scipy.io as sio 
import os
import numpy as np 
import matplotlib.pyplot as plt 

subs = [101, 102]
#fall 2018
subs = [101, 102, 103, 104, 105, 106, 108, 109, 110, 111, 112,
        202, 203, 204, 205, 207, 208, 209, 210, 211, 
        301, 302, 303, 304, 305, 306, 307, 308, 309]
#winter 2019
subs = [1101, 1102, 1103, 1104, 1105, 1106, 1108, 1109, 1110,
        1202, 1203, 1205, 1206, 1209, 1210, 1211, 1215,
        1301, 1302, 1313, 
        1401, 1402, 1403, 1404, 1405,  1408, 1410, 1411, 1412, 1413, 1413, 1414, 1415, 1416]
#both
subs = [101, 102, 103, 104, 105, 106, 108, 109, 110, 111, 112,
        202, 203, 204, 205, 207, 208, 209, 210, 211, 
        301, 302, 303, 304, 305, 306, 307, 308, 309,
        1101, 1102, 1103, 1104, 1105, 1106, 1108, 1109, 1110,
        1202, 1203, 1205, 1206, 1209, 1210, 1211, 1215,
        1301, 1302, 1313, 
        1401, 1402, 1403, 1404, 1405,  1408, 1410, 1411, 1412, 1413, 1413, 1414, 1415, 1416]

n_subs = len(subs)
n_sesh = 2
conditions = ['valid','invalid']
n_cond = len(conditions)

# cutoff trials that are too slow or fast
rt_toofast = 250
rt_tooslow = 1500

#creates arrays to save output
count_rt = np.zeros((n_subs, n_sesh, n_cond))
median_rt = np.zeros((n_subs, n_sesh, n_cond))
prop_accu = np.zeros((n_subs, n_sesh, n_cond))

# loop through subjects
for isub, sub in enumerate(subs):
	print('Subject - ' + str(sub))

	for sesh in range(n_sesh):
		print('Session - ' + str(sesh+1))
		
		# get the path and file name and load data
		path =  './subject' + str(sub) + '/session' + str(sesh+1) + '/'
		file =  [x for x in os.listdir(path) if x.endswith('.mat')]
		output_dict = sio.loadmat(path + file[0])

		# pull out important stuff
		output = output_dict['output']
		accuracy = output[:,6]
		rt = output[:,7]
		validity = output[:,3]

		# count each type of trial
		count_rt[isub,sesh,:] 	= [len( rt[(validity == 1) & 
										(rt >= rt_toofast) &
										(rt <= rt_tooslow)]), 
								   len( rt[(validity == 0) &
										(rt >= rt_toofast) &
										(rt <= rt_tooslow)]) ]
		# median rt on each condition	
		median_rt[isub,sesh,:] 	= [ np.nanmedian ( rt [ (validity == 1) &
													 	(rt >= rt_toofast) &
													 	(rt <= rt_tooslow)]),
									np.nanmedian ( rt [ (validity == 0) &
														(rt >= rt_toofast) &
														(rt <= rt_tooslow)]) ]
		# proportion accurate (number accurate / count)							
		prop_accu[isub,sesh,:]  = [	np.sum ( accuracy [ (validity == 1) &
														(rt >= rt_toofast) &
														(rt <= rt_tooslow)]) / 
									np.sum((validity == 1) & (rt >= rt_toofast) & (rt <= rt_tooslow)),

									np.sum ( accuracy [ (validity == 0) &
														(rt >= rt_toofast) &
														(rt <= rt_tooslow)]) /
									np.sum((validity == 0) & (rt >= rt_toofast) & (rt <= rt_tooslow)) ]
	

# Summary states and collapse sessions
Out_count = np.squeeze(np.sum(count_rt,axis=1))
Out_median_RT = np.squeeze(np.nanmean(median_rt,axis=1))
Out_prop_accu = np.squeeze(np.nanmean(prop_accu,axis=1))

print(Out_count)
print(Out_median_RT)
print(Out_prop_accu)



# T-test 

# bar plot results
plt.figure()
# Accuracy
ax = plt.subplot(211)
plt.bar([0,1], np.nanmean(Out_prop_accu,axis=0), 0.6, yerr = np.nanstd(Out_prop_accu,axis=0)/np.sqrt(n_subs))
plt.ylim(.9,.96)
plt.title('Accuracy')
plt.ylabel('Proportion Correct')
ax.set_xticks([0,1])
ax.set_xticklabels(conditions)
# RT
ax = plt.subplot(212)
plt.bar([0,1], np.nanmean(Out_median_RT,axis=0), 0.6, yerr = np.nanstd(Out_median_RT,axis=0)/np.sqrt(n_subs))
plt.ylim(450,600)
plt.title('Reaction Time')
plt.ylabel('RT (ms)')
plt.xlabel('Condition')
ax.set_xticks([0,1])
ax.set_xticklabels(conditions)
plt.show()

print('Done')
