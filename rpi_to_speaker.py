# Python libraries
import pygame

# plays the test.wav file
pygame.mixer.init()
pygame.mixer.music.load("test.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue