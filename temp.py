# Get positive frequency
idx = np.where(freq > 0)[0]
freq = freq[idx]
sp = sp[idx]

# Get dominant frequencies
sort = np.argsort(-abs(sp.real))[:100]
dom_freq = freq[sort]

# Round and calculate amplitude ratio
freq_ratio = np.round(dom_freq/frequency)
unique_freq_ratio = np.unique(freq_ratio)
amp_ratio = abs(sp.real[sort]/np.sum(sp.real[sort]))
factor = np.zeros((int(unique_freq_ratio[-1]), ))
for i in range(factor.shape[0]):
    idx = np.where(freq_ratio==i+1)[0]
    factor[i] = np.sum(amp_ratio[idx])
factor = factor/np.sum(factor)

def apply_overtones(frequency, duration, factor, sample_rate=44100, amplitude=4096):

    assert abs(1-sum(factor)) < 1e-8
    
    frequencies = np.minimum(np.array([frequency*(x+1) for x in range(len(factor))]), sample_rate//2)
    amplitudes = np.array([amplitude*x for x in factor])
    
    fundamental = get_sine_wave(frequencies[0], duration, sample_rate, amplitudes[0])
    for i in range(1, len(factor)):
        overtone = get_sine_wave(frequencies[i], duration, sample_rate, amplitudes[i])
        fundamental += overtone
    return fundamental

# Construct harmonic series
note = apply_overtones(frequency, duration=2.5, factor=factor)

def get_adsr_weights(frequency, duration, length, decay, sustain_level, sample_rate=44100):

    assert abs(sum(length)-1) < 1e-8
    assert len(length) ==len(decay) == 4
    
    intervals = int(duration*frequency)
    len_A = np.maximum(int(intervals*length[0]),1)
    len_D = np.maximum(int(intervals*length[1]),1)
    len_S = np.maximum(int(intervals*length[2]),1)
    len_R = np.maximum(int(intervals*length[3]),1)
    
    decay_A = decay[0]
    decay_D = decay[1]
    decay_S = decay[2]
    decay_R = decay[3]
    
    A = 1/np.array([(1-decay_A)**n for n in range(len_A)])
    A = A/np.nanmax(A)
    D = np.array([(1-decay_D)**n for n in range(len_D)])
    D = D*(1-sustain_level)+sustain_level
    S = np.array([(1-decay_S)**n for n in range(len_S)])
    S = S*sustain_level
    R = np.array([(1-decay_R)**n for n in range(len_R)])
    R = R*S[-1]
    
    weights = np.concatenate((A,D,S,R))
    smoothing = np.array([0.1*(1-0.1)**n for n in range(5)])
    smoothing = smoothing/np.nansum(smoothing)
    weights = np.convolve(weights, smoothing, mode='same')
    
    weights = np.repeat(weights, int(sample_rate*duration/intervals))
    tail = int(sample_rate*duration-weights.shape[0])
    if tail > 0:
        weights = np.concatenate((weights, weights[-1]-weights[-1]/tail*np.arange(tail)))
    return weights

# Get sound wave
note = apply_overtones(frequency, duration=2.5, factor=factor)

# Apply smooth ADSR weights
weights = get_adsr_weights(frequency, duration=2.5, length=[0.05, 0.25, 0.55, 0.15], decay=[0.075,0.02,0.005,0.1], sustain_level=0.1)

# Write to file
data = note*weights
data = data*(4096/np.max(data)) # Adjusting the Amplitude 
wavfile.write('final.wav', sample_rate, data.astype(np.int16))