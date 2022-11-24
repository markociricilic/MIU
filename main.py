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
split_signal = np.split(single_fullprogression,5) # Split 
duration_of_signal = len(split_signal[1])
print("length of signal: ")
print(duration_of_signal)

#split audio signal into 5 equal lengths for short time FFT
split_signal = np.split(single_fullprogression,5) #split_signal[0] --> C major chord hopefully
signal_length = len(split_signal[1])
print("Length of signal(elements in vector): ", signal_length)

#FFT generation
N = np.arange(split_signal[1].shape[0])    # Number of points on the FFT
freq = np.fft.rfftfreq(N.shape[-1])*Fs             # Frequency
index_cut = int(2000/Fs * len(freq))
FP = np.fft.rfft(split_signal[1])           # FFT of G Major chord
# Plot spectrum
plt.plot(freq, abs(FP))
#plt.xlim([0, 2000])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of Chord Progression')
plt.grid()

#Find peaks of FFT spectrum
peaks,_ = find_peaks(abs(FP),height=0)
length_peak= len(peaks)
peak_values = abs(FP[peaks])
sorted_peak_values= np.sort(peak_values)
print(length_peak)
print(peaks)
print(sorted_peak_values)

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
