import network
from utime import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID","Password")
sleep(0.5)

if wlan.isconnected() == True:
    print('There you go!')
    print('giddy-up')
    print('you got connected in the 1st try')
    print('Your IP addr is: ', wlan.ifconfig()[0])
else:
    print('connection failed')
    print('next attempt...')
    sleep(3)
    wlan.connect("SSID","Password")
    if wlan.isconnected() == True:
        print('There you go!')
        print('giddy-up')
        print('you got connected in the 2nd try')
        print('Your IP addr is: ', wlan.ifconfig()[0])
    else:
        print('connection failed')
        print('next attempt...')
        sleep(2)
        wlan.connect("SSID","Password")
        if wlan.isconnected() == True:
            print('There you go!')
            print('giddy-up')
            print('you got connected in the 3rd try')
            print('Your IP addr is: ', wlan.ifconfig()[0])
        else:
            print("didn't work, run the script again")
            print('check is your Wi-Fi is working')
            print("then check the user&pass that you've used")
