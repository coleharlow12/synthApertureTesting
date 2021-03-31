import serial
import time

#ser = serial.Serial('/dev/tty.usbmodem14201', 115200) # Used on MAC
ser = serial.Serial(port = "COM13", baudrate=115200)

time.sleep(2)
ser.write(b'G28\r\n')

readSer=True
while readSer:
	a=ser.readline().decode('UTF-8')
	if a=="ok\n":
		readSer=False

ser.write(b'G1 X200.000 Y10.000 E0 F12000\r\n')

readSer=True
while readSer:
	a=ser.readline().decode('UTF-8')
	print(a)
	if a=="ok\n":
		readSer=False

ser.write(b'G1 X0 Y10.000 E0 F12000\r\n')

readSer=True
while readSer:
	a=ser.readline().decode('UTF-8')
	print(a)
	if a=="ok\n":
		readSer=False
		
ser.close()