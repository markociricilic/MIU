#%%

# Algorithm for melody extraction and playback

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# Load data from G Major Chord wav file
Fs, gmajor = wavfile.read('Chord Extraction/gmajor.wav')
single_gmajor = gmajor[:,1]; # Single channel

# N = len(single_gmajor); # Number of points on the FFT

#FFT
N = np.arange(single_gmajor.shape[0])   # Number of points on the FFT
freq = np.fft.fftfreq(N.shape[-1])*Fs   # Frequency
G = np.fft.fft(single_gmajor)           # FFT of G Major chord

# Plot spectrum
plt.plot(freq, abs(G))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of G Major Chord')
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