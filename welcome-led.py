from machine import Pin
from time import sleep

Bled = Pin(16, Pin.OUT)
Rled = Pin(17, Pin.OUT)
Gled = Pin(18, Pin.OUT)


def LEDwelcome():
    while True:
        Bled.value(1)
        sleep(0.3)
        Gled.value(1)
        sleep(0.3)
        Rled.value(1)
        sleep(0.3)
        Bled.value(0)
        Gled.value(0)
        Rled.value(0)
        sleep(0.5)
    
LEDwelcome()
