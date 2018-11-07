clear

[filename, pathname] = uigetfile('*.mat')
load([pathname filename])

accuracy = output(:,7)
rt = output(:,8)
validity = output(:,4)
conditions = {'valid', 'invalid'}
mean_rt = [mean(rt(validity == 1)) mean(rt(validity == 0))]
median_rt = [median(rt(validity == 1)) median(rt(validity == 0))]
mean_accuracy = [sum(accuracy(validity == 1))/sum(validity == 1) sum(accuracy(validity == 0))/sum(validity == 0)]

