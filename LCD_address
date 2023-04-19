import machine
sda = machine.Pin(8)
scl = machine.Pin(9)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

print(hex(int(str(i2c.scan())[1:-1])))
