#%%

# Algorithm for melody extraction and playback

import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# Load data from chord progression
Fs, fullprogression = wavfile.read('Chord Extraction/fullprogression.wav')
single_fullprogression = fullprogression[:,1] # Single channel
split_signal = np.split(single_fullprogression,5) # Split 
duration_of_signal = len(split_signal[1])
print("length of signal: ")
print(duration_of_signal)

#FFT
N = np.arange(split_signal[1].shape[0])    # Number of points on the FFT
freq = np.fft.fftfreq(N.shape[-1])*Fs             # Frequency
FP = np.fft.fft(split_signal[1])           # FFT of G Major chord

peaks = find_peaks(abs(FP.real))
peaks_sorted = np.sort(peaks)
print(peaks_sorted)

# Plot spectrum
plt.plot(freq, abs(FP))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of Chord Progression')
plt.xlim((0, 2000))
plt.grid()
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
