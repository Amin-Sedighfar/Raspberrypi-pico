from machine import Pin,PWM
from utime  import sleep_ms

sound = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Port internal pull-down

led = Pin(16, Pin.OUT) 

 
if __name__ == '__main__':
    while True:
        if sound.value() == 1:
            led.high()
            sleep_ms(200)
        else:
            led.low()
