from machine import Pin, PWM

# buttonPIN = 15
# ledPIN = 16
# buzzerPIN = 18

buzzer = PWM(Pin(18))
buzzer.freq(500)
led = Pin(16, Pin.OUT) 
button = Pin(15, Pin.IN, Pin.PULL_UP) # Internal pull-up
led.value(0)


while True:
    if button.value() == 0:
        buzzer.duty_u16(12000) # volume between 10 to 12000
        led.high()
    else:
        buzzer.duty_u16(0) # volume between 10 to 12000
        led.low()
