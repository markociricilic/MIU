#%%

# Algorithm for melody extraction and playback

import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# Load data from Chord Progression wav file
Fs, fullprogression = wavfile.read('Chord Extraction/fullprogression.wav')
single_fullprogression = fullprogression[:,1] # Single channel
split_signal = np.split(single_fullprogression,5)
#split_signal[0] --> C major chord hopefully
#split_signal[1] --> F major chord hoepfully .....
duration_of_signal = len(split_signal[1])
print("length of signal: ")
print(duration_of_signal)

#FFT
N = np.arange(split_signal[1].shape[0])    # Number of points on the FFT
freq = np.fft.fftfreq(N.shape[-1])*Fs      # Frequency
FP = np.fft.fft(split_signal[1])           # FFT of G Major chord

peaks, _ = find_peaks(abs(FP))
peaks_sorted = sorted(zip(peaks, freq), reverse=True)[:5]
print(peaks_sorted)

# Plot spectrum
plt.plot(freq, abs(FP))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of Chord Progression')
plt.xlim((0, 2000))
plt.grid()
# %%