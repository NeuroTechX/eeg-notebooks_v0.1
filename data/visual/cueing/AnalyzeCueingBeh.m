clear

subs = {'101' '102' '103' '104' '105' '106' '108' '109' '110' '111' '112' ...
        '202' '203' '204' '205' '207' '208' '209' '210' '211' ...
        '301' '302' '303' '304' '305' '306' '307' '308' '309'};
    
n_subs = length(subs);
n_sesh = 2; %ran two blocks each  
n_cond = 2; %valid and invalid
count_rt = zeros(n_subs,n_sesh,n_cond);
median_rt = zeros(n_subs,n_sesh,n_cond);
mean_accuracy = zeros(n_subs,n_sesh,n_cond);
conditions = {'valid', 'invalid'};

for i_sub = 1:n_subs
    sub = subs{i_sub};
    fprintf(['Subject - ' sub '. \n']);
    
    for i_sesh = 1:n_sesh       
        pathname = ['~/eeg-notebooks/data/visual/cueing/subject' sub '/session' num2str(i_sesh) '/'];
        W = what(pathname);
        filename = W.mat{1};
        load([pathname filename])


        accuracy = output(:,7);
        rt = output(:,8);
        validity = output(:,4);

        rt_toofast = 250;
        rt_tooslow = 1500;

        count_rt(i_sub,i_sesh,:) = [length(rt(validity == 1 & rt >= rt_toofast & rt <= rt_tooslow)) ...
                                    length(rt(validity == 0 & rt >= rt_toofast & rt <= rt_tooslow))];
        median_rt(i_sub,i_sesh,:) = [nanmedian(rt(validity == 1 & rt >= rt_toofast & rt <= rt_tooslow)) ...
                                     nanmedian(rt(validity == 0 & rt >= rt_toofast & rt <= rt_tooslow))];
        mean_accuracy(i_sub,i_sesh,:) = [sum(accuracy(validity == 1 & rt >= rt_toofast & rt <= rt_tooslow))/sum(validity == 1 & rt >= rt_toofast & rt <= rt_tooslow) 
                                         sum(accuracy(validity == 0 & rt >= rt_toofast & rt <= rt_tooslow))/sum(validity == 0 & rt >= rt_toofast & rt <= rt_tooslow)];

    end
end
%% Summary stats and collapse sessions
Out_count = squeeze(sum(count_rt,2));
Out_median_RT = squeeze(nanmean(median_rt,2));
Out_mean_accuracy = squeeze(nanmean(mean_accuracy,2));
nanmean(Out_median_RT)
nanmean(Out_mean_accuracy)

[H,P,CI,stats] = ttest(Out_median_RT(:,1),Out_median_RT(:,2))
[H,P,CI,stats] = ttest(Out_mean_accuracy(:,1),Out_mean_accuracy(:,2))



%% Barplot of Results
figure; 
subplot(1,2,1);
barweb(nanmean(Out_mean_accuracy),nanstd(Out_mean_accuracy)/sqrt(n_subs));
ylim([.8 1])
title('Accuracy')
subplot(1,2,2);
barweb(nanmean(Out_median_RT),nanstd(Out_median_RT)/sqrt(n_subs));
ylim([300 700])
title('Reaction Time');
legend(conditions);


%% Barplot of Results
figure; 
subplot(1,2,1);
plot(Out_mean_accuracy');
title('Accuracy')
subplot(1,2,2);
plot(Out_median_RT');
title('Reaction Time');


%% Xcell output
LastName = subs;
AccValid = Out_mean_accuracy(:,1);
AccInvalid = Out_mean_accuracy(:,2);
RTValid = Out_median_RT(:,1);
RTInvalid = Out_median_RT(:,2);

T = table(AccValid,AccInvalid,RTValid,RTInvalid,...
    'RowNames',LastName)

writetable(T,'375CueingBeh.csv','WriteRowNames',true)  


