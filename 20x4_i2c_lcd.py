from machine import I2C
from time import sleep
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# HELP
# lcd.display_on()
# lcd.display_off()
# lcd.backlight_off()
# lcd.backlight_on()
# lcd.blink_cursor_on()
# lcd.blink_cursor_off()
# lcd.clear()
# lcd.move_to(1,1)
# lcd.putchar(chr(0))

lcd.custom_char(0, bytearray([0x00, 0x00, 0x0A, 0x00, 0x11, 0x0E, 0x00, 0x00])) # smily face
lcd.custom_char(1, bytearray([0x00, 0x00, 0x0A, 0x00, 0x0E, 0x11, 0x00, 0x00])) # sad face
lcd.custom_char(2, bytearray([0x04, 0x0A, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04])) # question mark
lcd.custom_char(3, bytearray([0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04])) # exclamation mark
lcd.custom_char(4, bytearray([0x00, 0x0A, 0x1F, 0x1F, 0x1F, 0x0E, 0x04, 0x00])) # heart
lcd.custom_char(5, bytearray([0x1F, 0x11, 0x0A, 0x04, 0x04, 0x0A, 0x11, 0x1F])) # hourglass
lcd.custom_char(6, bytearray([0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x00, 0x00])) # multiply
lcd.custom_char(7, bytearray([0x04, 0x0E, 0x0E, 0x0E, 0x0E, 0x1F, 0x00, 0x04])) # bell
lcd.custom_char(8, bytearray([0x00, 0x00, 0x01, 0x03, 0x16, 0x1C, 0x18, 0x00])) # tick
lcd.custom_char(9, bytearray([0x10, 0x18, 0x1C, 0x1E, 0x1C, 0x18, 0x10, 0x00])) # play


lcd.write_line("    Howdy Guys?",0)
lcd.move_to(15,0)
lcd.putchar(chr(2))
lcd.move_to(16,0)
lcd.putchar(chr(3))
lcd.move_to(17,0)
lcd.putchar(chr(4))
lcd.write_line("   Don't forget to ",1)
lcd.write_line("Subs. me on YouTube",2)
lcd.move_to(19,2)
lcd.putchar(chr(9))
lcd.write_line("   Amin Sedighfar",3)
lcd.move_to(18,3)
lcd.putchar(chr(0))

# while 85>75:
#     lcd.display_on()
#     sleep(0.7)
#     lcd.display_off()
#     sleep(0.7)
