from machine import Pin, UART, PWM
import utime
import pygame

#Pinouts & Setup Declaration
uart = UART(0,9600)         #Sets baudrate to 9600 meaning that the serial port is capable of transferring a maximum of 9600 bits per second
speaker = PWM(Pin(16))      #Connecting the speaker to the GP16

pygame.mixer.init()
pygame.mixer.music.load("test.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue