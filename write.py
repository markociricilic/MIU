# Write to file
data = note*weights
data = data*(4096/np.max(data)) # Adjusting the Amplitude 
wavfile.write('final.wav', sample_rate, data.astype(np.int16))
