from machine import Pin, PWM, I2C
from pico_i2c_lcd import I2cLcd
import urequests as requests
from utime import sleep
import json

# Global Varibales related to Mist
mist_token = 'Your_MIST_Token'
api_get_url = "Your_Mist_Get_Url_With_Org-id"
api_put_url = "Your_Mist_Put_Url_With_Org-id"
payload = {}
false_payload = json.dumps({"ssid": "SSID", "enabled": False})
true_payload = json.dumps({"ssid": "SSID", "enabled": "True"})
headers = {"Content-Type": "application/json", "Authorization": f"Token {mist_token}"}

# RaspberryPi pins
button = Pin(15, Pin.IN, Pin.PULL_UP) # Internal pull-up
led = Pin(16, Pin.OUT)
buzzer = PWM(Pin(18))
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
lcd.custom_char(2, bytearray([0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x00, 0x00])) # multiply
lcd.custom_char(3, bytearray([0x04, 0x0E, 0x0E, 0x0E, 0x0E, 0x1F, 0x00, 0x04])) # bell


def MistGet():
    try:
        get_response = requests.get(api_get_url, headers=headers, data=payload)
        wlans = json.loads(get_response.text)
        for wlan in wlans:
            if wlan['ssid'] == "SSID":
                return wlan['enabled']
    except:
        print(f"Can't get Mist data: {get_response.status_code}")

def MistPut(newstate):
    requests.request("PUT", api_put_url, headers=headers, data=newstate)

while True:
    sleep(0.2)
    if button.value() == 0:
        lcd.clear()
        buzzer.duty_u16(12000)
        lcd.write_line("Change Request",0)
        lcd.move_to(15,0)
        lcd.putchar(chr(3))
        sleep(0.2)
        buzzer.duty_u16(0)
        print("A Change Command Just Received")
        print("-" * 30)
        if MistGet() == "True":
            print('Current SSID state: on')
            print('wait up....')
            print("-" * 30)
            MistPut(newstate=false_payload)
#             sleep(1)
            if MistGet() == "True":
                print(" SSID new Status: on")
                led.high()
                print("-" * 30)
            else:
                print(" SSID new Status: off")
                led.low()
                print("-" * 30)
        else:
            print('Current SSID state: off')
            print('wait up....')
            print("-" * 30)
            MistPut(newstate=true_payload)
#             sleep(1)
            if MistGet() == "True":
                print(" SSID new Status: on")
                led.high()
                print("-" * 30)
            else:
                print(" SSID new Status: off")
                led.low()
                print("-" * 30)
