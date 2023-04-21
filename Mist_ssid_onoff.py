from machine import Pin, PWM, I2C
from pico_i2c_lcd import I2cLcd
import urequests as requests
from utime import sleep
import network
import json

# Global Varibales related to Mist
mist_token = 'YOUR_TOKEN'
api_get_url = "https://api.mist.com/api/..."
api_put_url = "https://api.mist.com/api/..."
payload = {}
false_payload = json.dumps({"ssid": "NAME", "enabled": False})
true_payload = json.dumps({"ssid": "NAME", "enabled": "True"})
headers = {"Content-Type": "application/json", "Authorization": f"Token {mist_token}"}

#Wi-Fi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID","PASSWORD")

# RaspberryPi pins
button = Pin(15, Pin.IN, Pin.PULL_UP) # Internal pull-up
Bled = Pin(16, Pin.OUT)
Rled = Pin(17, Pin.OUT)
Gled = Pin(18, Pin.OUT)
buzzer = PWM(Pin(19))
buzzer.freq(500)

# LCD Setup
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# LCD Characters
lcd.custom_char(0, bytearray([0x00, 0x00, 0x01, 0x03, 0x16, 0x1C, 0x18, 0x00])) # tick
lcd.custom_char(1, bytearray([0x1F, 0x11, 0x0A, 0x04, 0x04, 0x0A, 0x11, 0x1F])) # hourglass
lcd.custom_char(2, bytearray([0x04, 0x0E, 0x0E, 0x0E, 0x0E, 0x1F, 0x00, 0x04])) # bell
lcd.custom_char(3, bytearray([0x00, 0x00, 0x0A, 0x00, 0x11, 0x0E, 0x00, 0x00])) # smily face
lcd.custom_char(4, bytearray([0x00, 0x00, 0x0A, 0x00, 0x0E, 0x11, 0x00, 0x00])) # sad face
lcd.custom_char(5, bytearray([0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x00, 0x00])) # multiply

#LED states
def SSIDonState():
    Gled.high()
    Rled.low()

def SSIDoffState():
    Gled.low()
    Rled.high()

#Welcome LEDs Dance
def LEDwelcome():
    Bled.value(1)
    sleep(0.5)
    Gled.value(1)
    sleep(0.5)
    Rled.value(1)
    sleep(0.5)
    Bled.value(0)
    Gled.value(0)
    Rled.value(0)
    sleep(0.5)
    Bled.value(1)
    sleep(0.5)
    Gled.value(1)
    sleep(0.5)
    Rled.value(1)
    sleep(0.5)
    Bled.value(0)
    Gled.value(0)
    Rled.value(0)
    sleep(0.5)
    Bled.value(1)
    sleep(0.5)
    Gled.value(1)
    sleep(0.5)
    Rled.value(1)
    sleep(0.5)
    Bled.value(0)
    Gled.value(0)
    Rled.value(0)

# Pint on LCD
def PrintLCD(text,line):
    lcd.write_line(text,line)

def PrintChar(c,l,n):
    lcd.move_to(c,l)
    lcd.putchar(chr(n))
    
    
def MistGet():
    try:
        get_response = requests.get(api_get_url, headers=headers, data=payload)        
        wlan = json.loads(get_response.text)
        return wlan['enabled']
    except Exception as error:
        print(f"Can't get Mist data: {get_response.status_code}")

def MistPut(newstate):
    requests.request("PUT", api_put_url, headers=headers, data=newstate)
    
PrintLCD("Starting...",0)
LEDwelcome()
PrintLCD("Your IP Address:",0)
PrintLCD(wlan.ifconfig()[0],1)

while True:
    sleep(0.2)
    if button.value() == 0:
        lcd.clear()
        buzzer.duty_u16(12000)
        Bled.high()
        PrintLCD("Change Request",0)
        PrintChar(15,0,2)
        sleep(0.2)
        Bled.low()
        buzzer.duty_u16(0)
        if MistGet() == "True":
            PrintLCD("Current Wi-Fi: on",1)
            PrintChar(19,1,3)
            SSIDonState()
            PrintLCD("Wait up (changing)",2)
            PrintChar(19,2,1)
            MistPut(newstate=false_payload)
            if MistGet() == "True":
                PrintLCD("Previous Wi-Fi: on",1)
                PrintChar(19,1,3)
                PrinLCD("Current Wi-Fi: on",3)
                PrintChar(19,3,3)
                SSIDonState()
            else:
                PrintLCD("Previous Wi-Fi: on",1)
                PrintChar(19,1,3)
                PrintLCD("Current Wi-Fi: off",3)
                PrintChar(19,3,4)
                SSIDoffState()
        else:
            PrintLCD("Current Wi-Fi: off",1)
            PrintChar(19,1,4)
            SSIDoffState()
            PrintLCD("Wait up (changing)",2)
            PrintChar(19,2,1)
            MistPut(newstate=true_payload)
            if MistGet() == "True":
                PrintLCD("Previous Wi-Fi: off",1)
                PrintChar(19,1,4)
                PrintLCD("Current Wi-Fi: on",3)
                PrintChar(19,3,3)
                SSIDonState()
            else:
                PrintLCD("Previous Wi-Fi: off",1)
                PrintChar(19,1,4)
                PrintLCD("Current Wi-Fi: off",3)
                PrintChar(19,3,4)
                SSIDoffState()
