# eeg-notebooks
A collection of classic EEG experiments implemented for consumer EEG systems

### Visual P300 with Oddball paradigm
The visual P300 is a spike that occurs 300ms after perceiving a visual stimulus that has implications on decision making. This was validated in Muse by AB with the Oddball paradigm, in which low-probability target items (oddballs) are interspersed with high probability non-target items. With AB's paradigm, the experiment takes about 10 minutes to run (5 x 2 minute trials). The best pipeline for classifying P300s after collecting a dataset (for use in BCI) was found to be .77 AUC with  ERP Covariance + MDM (Riemannian Geometry based). This accuracy is apparently good but not outstanding as far as BCIs go.

Unfortunately, I've also heard from Hubert that, in testing 10 different people, some of them weren't able to get very good ERPs. This could be due to their neuroanatomy, as EEG expresses pretty differently between people. Additionally, a follow-up notebook comparing accuracy between subjects showed decreased accuracy (.64 AUC)

### Auditory P300
Same as the visual P300, but dependent on auditory stimulus. Auditory P300s are normally less distinguishable than visual P300s, but they may be more suited to the Muse since its electrodes are closer to auditory centers (superior temporal cortex). AB's validation of this produced a .63 AUC score

### C1 and P1
C1 and P1 are two ERPs related to the perceiving of visual stimulus. The C1 is the first component, appearing in the 65-90ms range after stimulus onset while the P1 appears later, around 100ms.

C1 and P1 were validated in Muse by Hubert, who performed a left/right visual field experiment. Comparing ERPs to left or right-field presentation of visual stimuli revealed a contralateral pattern of C1 and P1 in the both the temporal and anterior electrodes. However, their timing seems a little delayed

### N170
The N170 is an ERP specifically related to the perception of faces. This was validated in Muse by Hubert with a 12 minute experiment (6 x 2 minute trials). Stimuli consisted of 12 pictures of houses and 12 pictures of faces. A N170 around 200ms was found with a classification AUC of .7

### SSAEP
The steady state auditory evoked potential is a frequency response produced when hearing modulating tones of certain frequencies. It was validated in Muse by Hubert, who used 45hz and 40hz amplitude modulation applied to 900 and 770h carrier frequencies. A PSD of the produced EEG signal showed clear spikes, correspondingly, at 45 and 40hz in the temporal electrodes. He also noticed a clear N100 and P200 complex in at the beginning of stimulus onset 

## SSVEP
The steady state visual evoked potential is a frequency response produced visual stimulation at specific frequencies. It was validated by Hubert in a 12 minute experiment (6 x 2 minute trials). Stimulation frequencies of 30hz and 20hz were used and an extra electrode at POz was added. Found clear peaks in the PSD at the stimulation frequencies. The peaks were most significant at the extra electrode, which is closest to the primary visual regions, but was detectable at all electrodes and found to have an accuracy of .95 AUC when using a filter bank approach to isolate specific frequencies. 


## Unvalidated Experiments and other phenomena

### N100 - P200
The combination of a negative evoked potential around 100ms after any unpredictable stimulus and a positive potential 200ms after. These were noticed inHubert's SSAEP experiment, but not independently classified or tested.

### On-task Beta
Noticed in Hubert's visual grating test, but difficult to extract.

### Alpha reset
A noticeable increase in alpha activity after stimulus presentation ends. Noticed in Hubert's visual grating test.

## Other details related to Muse ERP analysis

- Latency and jitter related to BLE data transmission is 40ms +-20ms
- In Krigolson lab's resampling analysis, a sample size of 10 was found to be needed for high statistical accuracy for N200 and reward positivity, which is similar to traditional EEG, but the sample size needed to be greater for P300
- Krigolson notes difficulties marking EEG streams with the OSC protocol because of time lag in the event stream as well. In the end they elected to creat recordings starting at the beginning of each stimulus onset
