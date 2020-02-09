#Sending an SMS
import time
import serial
          
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print("Command : AT+IPR=115200")
ser.write('AT+IPR=115200'+'\r\n')
rcv=ser.read(10)
print(rcv)
time.sleep(1)
print("1st done! : Baudrate set")
print("=========================")

print("Command : AT+CMGF=1")
ser.write('AT+CMGF=1'+'\r\n')
rcv=ser.read(10)
print(rcv)
time.sleep(1)
print("2nd done! : set to TEXT mode")
print("=========================")

print("Command : AT+CMGS=+947")
ser.write('AT+CMGS="+94702130478"'+'\r\n')
rcv=ser.read(10)
print(rcv)
time.sleep(1)
print("3rd done! : Set phone number to send SMS")
print("=========================")

ser.write('SMS Hello'+'\r\n')
rcv=ser.read(10)
print(rcv)
print("4th done! : Message to be sent > SMS Hello")
print("=========================")

ser.write('\x1A')
for i in range(10):
    rcv=ser.read(10)
    print(rcv)
    
print("5th done! : Message sent")
print("=========================")
    
      
    
    


