from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
 
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.move_to(0,0)
lcd.putstr("Hey Guys")
lcd.move_to(0,1)
lcd.putstr("How's it going?")
