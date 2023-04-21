from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(18))
buzzer.freq(500)
buzzer.duty_u16(12000) # volume between 10 to 12000
sleep(0.5)
buzzer.duty_u16(0)
sleep(0.5)

buzzer.duty_u16(12000) # volume between 10 to 12000
sleep(0.5)
buzzer.duty_u16(0)
sleep(0.5)

buzzer.duty_u16(12000) # volume between 10 to 12000
sleep(0.5)
buzzer.duty_u16(0)
sleep(0.5)

buzzer.duty_u16(12000) # volume between 10 to 12000
sleep(0.5)
buzzer.duty_u16(0)
