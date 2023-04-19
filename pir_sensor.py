from machine import Pin

PIR = Pin(28,Pin.IN)
led = Pin(16,Pin.OUT)

while True:
    if PIR.value() == 1:
        
        led.value(1)
        
    else:
        led.value(0)
