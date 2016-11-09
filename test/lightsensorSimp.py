import smbus
from Adafruit_I2C import Adafruit_I2C
import time

Light_sensor = Adafruit_I2C(0x29, 2)

while(True):
    buff = 0x8c
    wordval = Light_sensor.readU16(buff)
    newval = Light_sensor.reverseByteOrder(wordval)
    print("I2C:: returned 0x%04X" % (wordval))
    time.sleep(.2)