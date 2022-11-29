#%%
# Algorithm for melody extraction and playback
import numpy as np
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq
from scipy.fft import fft
from scipy.signal import find_peaks
import random
import math
import matplotlib.pyplot as plt
from pydub import AudioSegment

#pure_tone generator
def pure_tone_generator(frequency, duration, sample_rate = 44100, amplitude = 4096):
    if frequency >= 1000:
        amplitude = 0
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

def range_num_generator(random_duration_index):
    if random_duration_index == 0:
        range_num = Fs
    elif random_duration_index == 1:
        range_num = Fs/2
    else:
        range_num = Fs/4 

    return int(range_num)

#Style of plot for testing and debugging
plt.style.use('seaborn-v0_8')

# Load data from Full Progression wav file
Fs, fullprogression = wavfile.read('Chord Extraction/fullprogression.wav')
single_fullprogression = fullprogression[:,1] # Single channel

t_full = np.arange(0,24,1/44100)

specified_sub_divisions = 20 #how many sections to split fullprogression
notes_distribution_constant = 100 #how many peak frequencies to extract and put into frequency matrix per segment

fullprogression_time = len(single_fullprogression)*(1/Fs)
segment_time = fullprogression_time/specified_sub_divisions
floor_total_time = math.floor(segment_time)
dummy_note_time = math.ceil(10*(segment_time - floor_total_time))/10
print("full progression vector length: ", len(single_fullprogression))
print("full progression time in seconds: ", len(single_fullprogression)*(1/Fs))
print("segment_time in seconds: ", segment_time)
print("math floor function result", math.floor(segment_time))
print("dummy note time: ", dummy_note_time)


frequency_matrix = np.zeros([specified_sub_divisions,notes_distribution_constant],dtype=int)#top 100 dominant frequencies from each segment is contained in this frequency matrix. 
#frequency_matrix[0] --> accesses first segment dominant frequencies

#main_melody_vector definition
main_melody_vector = np.zeros([len(single_fullprogression)])
notes_duration_vector = [0.25,0.5,1.0] #notes_duration_vector[2] is quarter note time 
t_quarter = np.arange(0,1,1/44100)

#print("quarter time vector: ",t_quarter)
print("length of quarter vector", len(t_quarter))
t_eighth = np.arange(0,0.5,1/44100)
#print("t_eighth: ", t_eighth)
print("length of eighth vector", len(t_eighth))
t_sixteenth = np.arange(0,0.25,1/44100)
#print("t_sixteenth: ", t_sixteenth)
print("length of eighth vector", len(t_sixteenth))

wave= pure_tone_generator(440, notes_duration_vector[1],44100,1)
print("length of wave: ", len(wave))
plt.plot(t_eighth,wave)

print("main_melody_matrix length", len(main_melody_vector))

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
    top_ten_freq = dom_freq[-notes_distribution_constant : ]

    #store dominant frequencies in frequency_matrix
    for j in range(100):
        frequency_matrix[i][j] = top_ten_freq[j]

#print("frequency matrix: ", frequency_matrix)

###################################################################################
# Melody Generation Routine
# 1. random seeds
# 2. while loop logic
# 3. appending sub melody vector to main vector
###################################################################################

t_sub = np.arange(0,2.4,1/44100)

for i in range(specified_sub_divisions):
    sub_melody_vector_length = len(split_signals[i])
    sub_melody_vector = np.zeros(sub_melody_vector_length)
    #dummy note zero padding
    sub_melody_vector_length -= dummy_note_time*Fs
    index_for_appending = dummy_note_time*Fs

    while sub_melody_vector_length > 0:
        #generate number from 0 to 2 for random note duration
        if sub_melody_vector_length >= len(t_quarter):
            #generate number from 0 to 2 for random note duration
            random_duration_index = random.randint(0,2)
            random_frequency_index = random.randint(0,99)
            random_wave = pure_tone_generator(frequency_matrix[i][random_frequency_index],notes_duration_vector[random_duration_index],Fs,1)
             #appending 
            range_num = len(random_wave)
            for j in range(range_num):
                index = j+index_for_appending
                sub_melody_vector[int(index)] = random_wave[j]

            index_for_appending += range_num
            sub_melody_vector_length -= range_num
            
        elif sub_melody_vector_length >= len(t_eighth):
            #generate number from 0 to 1 for duration

            random_duration_index = random.randint(0,1)
            random_frequency_index = random.randint(0,99)
            random_wave = pure_tone_generator(frequency_matrix[i][random_frequency_index],notes_duration_vector[random_duration_index],Fs,1)
            
            #appending 
            range_num = len(random_wave)
            for j in range(range_num):
                index = j+index_for_appending
                sub_melody_vector[int(index)] = random_wave[j]

            index_for_appending += range_num
            sub_melody_vector_length -= range_num
        else:
            random_frequency_index = random.randint(0,99)
            #use sixteenth note duration
            random_wave = pure_tone_generator(frequency_matrix[i][random_frequency_index],notes_duration_vector[0],Fs,1)
            
            #appending 
            range_num= len(random_wave)
            for j in range(range_num):
                index = j+index_for_appending
                sub_melody_vector[int(index)] = random_wave[j]

            index_for_appending += range_num 
            sub_melody_vector_length -= range_num

    print(sub_melody_vector)
    #insert sub_melody_vector into main_melody_vector 
    beginning_index = len(sub_melody_vector)*i 
    for k in range(len(sub_melody_vector)):
        index = k + beginning_index
        main_melody_vector[int(index)] = sub_melody_vector[k]
    print("main: ", main_melody_vector)

# plt.plot(t_full,main_melody_vector)
# plt.xlim([0,24])
normalize_factor = np.max(np.abs(single_fullprogression),axis = 0)
normalized_single_fullprogression = single_fullprogression/normalize_factor
plt.plot(t_full,normalized_single_fullprogression)

complete = 0.5* main_melody_vector + 0.5 * normalized_single_fullprogression # Reducing amplitude of summed vectors

wavfile.write("test.wav", Fs, complete)
plt.plot(t_full, complete)

# %%
