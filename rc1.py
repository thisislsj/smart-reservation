# SIMSMS1.py

import RPi.GPIO as GPIO
import serial
import time, sys
import datetime

P_BUTTON = 24 # Button, adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

#SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(SERIAL_PORT, baudrate = 115200, timeout = 5)
setup()
ser.write('AT+CMGF=1'+'\r\n') # set to text mode

time.sleep(1)
print("set to text mode")
ser.write('AT+CMGDA="DEL ALL"\r') # delete all SMS 
time.sleep(1)
print("delete all SMS ")
reply = ser.read(ser.inWaiting()) # Clean buf
print("Listening for incomming SMS...")

while True:
    reply = ser.read(ser.inWaiting())
    if reply != "":
        ser.write('AT+CMGR=1'+'\r')
        time.sleep(1)
        reply = ser.read(ser.inWaiting())
        print("SMS received. Content:")
        print(reply)
