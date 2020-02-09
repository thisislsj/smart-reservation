#RECEIVE SMS ECEIVE
import time
import serial
          
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.write('AT+CMGF=1'+'\r\n') # set to text mode
time.sleep(1)
ser.write('AT+CMGDA="DEL ALL"\r') # delete all SMS 
time.sleep(1)
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