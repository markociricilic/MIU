#%%
# Algorithm for melody extraction and playback
import numpy as np
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq
from scipy.fft import fft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

#Style of plot for testing and debugging
plt.style.use('seaborn-v0_8')

# Load data from Full Progression wav file
Fs, fullprogression = wavfile.read('Chord Extraction/fullprogression.wav')
single_fullprogression = fullprogression[:,1] # Single channel

specified_sub_divisions= 10 #how many sections to split fullprogression
notes_distribution_constant = 100 #how many peak frequencies to extract and put into frequency matrix per segment

frequency_matrix= np.zeros([specified_sub_divisions,notes_distribution_constant],dtype=int)#top 100 dominant frequencies from each segment is contained in this frequency matrix. 
#frequency_matrix[0] --> accesses first segment dominant frequencies

#split audio signal into numsof subdivisions equal lengths for short time FFT
split_signals = np.split(single_fullprogression,specified_sub_divisions) #split_signal[0] --> C major chord hopefully

print("length")
#for loop routine for populating frequency_matrix
for i in range(10):
    #FFT generation
    N = np.arange(split_signals[i].shape[0])    # Number of points on the FFT
    freq = np.fft.rfftfreq(N.shape[0])*Fs             # Frequency
    FP = np.fft.rfft(split_signals[i])           # FFT of G Major chord
    
    #Dominant frequencies
    dom_freq = freq[np.argsort(abs(FP))]
    top_ten_freq= dom_freq[-notes_distribution_constant : ]

    #store dominant frequencies in frequency_matrix
    for j in range(100):
        frequency_matrix[i][j]=top_ten_freq[j]

print("frequency matrix: ", frequency_matrix)
#now we can start thinking about how to generate melody given the frequency_matrix .......



"""""
#FFT generation
N = np.arange(split_signals[1].shape[0])    # Number of points on the FFT
freq = np.fft.rfftfreq(N.shape[-1])*Fs             # Frequency
index_cut = int(2000/Fs * len(freq))
FP = np.fft.rfft(split_signals[1])           # FFT of G Major chord
# Plot spectrum
plt.plot(freq, abs(FP))
plt.xlim([0, 2000])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of Chord Progression')
plt.grid()

dom_freq = freq[np.argsort(abs(FP))]
n=100
top_ten_freq= dom_freq[-n : ]
print(top_ten_freq)
#Find peaks of FFT spectrum
peaks,_ = find_peaks(abs(FP),height=0)
length_peak= len(peaks)
peak_values = abs(FP[peaks])
sorted_peak_values= np.sort(peak_values)

print(peaks)
print(sorted_peak_values)
"""

# %%

""""
% F Major Chord
[fmajor, Fs] = audioread("fmajor.wav");
single_fmajor = fmajor(:,1); % Single channel
    
N = length(single_fmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_fmajor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of F Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(fmajor))")

% D Minor Chord
[dminor, Fs] = audioread("dminor.wav");
single_dminor = dminor(:,1); % Single channel

N = length(single_dminor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_dminor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of D Minor Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(dminor))")

% C Major Chord
[cmajor, Fs] = audioread("cmajor.wav");
single_cmajor = cmajor(:,1); % Single channel

N = length(single_cmajor); % Number of points on the FFT
f = (0:(N-1))*(Fs/N); % Frequency
X = fft(single_cmajor); % FFT of G Major chord

figure
plot(f, abs(X));
xlim([0 2000])
title("FFT of C Major Chord")
xlabel("Frequency (Hz)")
ylabel("real(fft(cmajor))")
"""
