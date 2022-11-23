#%%

# Algorithm for melody extraction and playback

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# Load data from wav file
sample_rate, middle_c = wavfile.read('Chord Extraction/cmajor.wav')

#FFT
t = np.arange(middle_c.shape[0])
freq = np.fft.fftfreq(t.shape[-1])*sample_rate
sp = np.fft.fft(middle_c) 

# Plot sound wave
plt.plot(middle_c[500:2500])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sound Wave of C Major on Piano')
plt.grid()

# Plot spectrum
plt.plot(freq, abs(sp.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of MC Major Recording on Piano')
plt.xlim((0, 2000))
plt.grid()
# %%
