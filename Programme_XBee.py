"""
Module DOC
"""
import time
import sys
sys.path.append('I2C-LCD')
import lcddriver
import RPi.GPIO as GPIO
from digi.xbee.devices import *
from digi.xbee.io import *
from digi.xbee.util import utils

API_URL = "https://api.thingspeak.com/update?api_key=ARZNLGR3N893AH58"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string("Mesure PANNEAU", 1)
lcd.lcd_display_string("IDDLE", 2)

#Instantiation de l'XBee Coord :
xbee_Coord = XBeeDevice("/dev/ttyAMA0", 9600)
xbee_Coord.open()

#Instantiation de l'XBee End Device :
xbee_ED = RemoteXBeeDevice(xbee_Coord, XBee64BitAddress.from_hex_string("0013A20041BF3D0D"))
xbee_ED.set_io_configuration(IOLine.DIO0_AD0, IOMode.DIGITAL_OUT_HIGH)

while True:

    if GPIO.input(16) == GPIO.LOW:
        time.sleep(0.5)
        print("Mesure en cours")
        xbee_ED.set_io_configuration(IOLine.DIO0_AD0, IOMode.DIGITAL_OUT_LOW)
        tension_bat = xbee_ED.read_io_sample()
        io_line = IOLine.DIO2_AD2
        print(tension_bat)
        time.sleep(1)
        xbee_ED.set_io_configuration(IOLine.DIO0_AD0, IOMode.DIGITAL_OUT_HIGH)

    #time.sleep(60)
    #xbee_ED.set_io_configuration(IOLine.DIO0_AD0, IOMode.DIGITAL_OUT_LOW)
    #tension_bat = xbee_ED_read_io_sample()
    #io_line = IOLine.DIO2_AD2
    #print(tension_bat)
