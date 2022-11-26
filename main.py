#%%
# Algorithm for melody extraction and playback
import numpy as np
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq
from scipy.fft import fft
from scipy.signal import find_peaks
from random import seed 
from random import random
import math
import matplotlib.pyplot as plt

#pure_tone generator
def pure_tone_generator(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

#Style of plot for testing and debugging
plt.style.use('seaborn-v0_8')

# Load data from Full Progression wav file
Fs, fullprogression = wavfile.read('Chord Extraction/fullprogression.wav')
single_fullprogression = fullprogression[:,1] # Single channel

specified_sub_divisions= 10 #how many sections to split fullprogression
notes_distribution_constant = 100 #how many peak frequencies to extract and put into frequency matrix per segment

fullprogression_time = len(single_fullprogression)*(1/Fs)
segment_time = fullprogression_time/specified_sub_divisions
floor_total_time = math.floor(segment_time)
dummy_note_time = math.ceil(10*(segment_time - floor_total_time))/10
print("full progression vector length: ", len(single_fullprogression))
print("split segment vector length: ", len(split_signals[0]))
print("full progression time in seconds: ",len(single_fullprogression)*(1/Fs))
print("segment_time in seconds: ", segment_time)
print("math floor function result", math.floor(segment_time))
print("dummy note time: ", dummy_note_time)


frequency_matrix= np.zeros([specified_sub_divisions,notes_distribution_constant],dtype=int)#top 100 dominant frequencies from each segment is contained in this frequency matrix. 
#frequency_matrix[0] --> accesses first segment dominant frequencies

#main_melody_vector definition
main_melody_vector = np.zeros([len(single_fullprogression)])
notes_duration_vector = [1, 0.5, 0.25] #notes_duration_vector[0] is quarter note
t_quarter = np.arange(0,1,1/44100)
print("quarter time vector: ",t_quarter)
print("length of quarter vector", len(t_quarter))
t_eighth = np.arange(0,0.5,1/44100)
print("t_eighth: ", t_eighth)
print("length of eighth vector", len(t_eighth))
t_sixteenth = np.arange(0,0.25,1/44100)
print("t_sixteenth: ", t_sixteenth)
print("length of eighth vector", len(t_sixteenth))

wave= pure_tone_generator(440, notes_duration_vector[1],44100,1)
print("length of wave: ", len(wave))
plt.plot(t_eighth,wave)
plt.xlim([0 ,0.1])

print("main_melody_matrix length", len(main_melody_matrix))

#split audio signal into numsof subdivisions equal lengths for short time FFT
split_signals = np.split(single_fullprogression,specified_sub_divisions) #split_signal[0] --> C major chord hopefully
print("sub segment length: ", len(split_signals[0]))

print("length")
#for loop routine for populating frequency_matrix
for i in range(specified_sub_divisions):
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

#print("frequency matrix: ", frequency_matrix)


#Melody Generation Routine
#1. random seeds
#2. while loop logic
#3. appending sub melody vector to main vector

for i in range(specified_sub_divisions):
    sub_melody_vector_length = len(split_signals[i])
    sub_melody_vector = np.zeros(sub_melody_vector_length)
    #dummy note zero padding
    sub_melody_vector_length-=dummy_note_time*Fs
    index_for_appending = dummy_note_time*Fs 
    while sub_melody_vector_length>0:
        

    #insert sub_melody_vector into main_melody_vector  




# %%
