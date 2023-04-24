from machine import Pin
from gpio_lcd import GpioLcd
 
# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16)

lcd.putstr('Hey Guys')
# lcd.clear()
# 0, x and 0, y location which is the top left-hand side.
lcd.move_to(0,1)
lcd.putstr("How's it going?")
# lcd.show_cursor()
# lcd.hide_cursor()
# lcd.blink_cursor_on()
# lcd.blink_cursor_off()
# lcd.display_off()
# lcd.display_on()
# lcd.backlight_off()
# lcd.backlight_on()
# lcd.putchar('Y')
# but this will only print 1 character
# happy_face = bytearray([0x00,0x0A,0x00,0x04,0x00,0x11,0x0E,0x00])
# lcd.custom_char(0, happy_face)
# lcd.putchar(chr(0))
