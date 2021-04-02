import os
import time
import serial
from pynput.mouse import Button, Controller
import sys
import numpy as np

mouse = Controller()

class Monkey(object):
	def __init__(self):
		self.filename= r'C:\ti\mmwave_studio_02_01_01_00\mmWaveStudio\PostProc\adc_data_Raw_0.bin'
		self.cached_stamp= os.stat(self.filename).st_mtime

	def ook(self):
		stamp = os.stat(self.filename).st_mtime
		if stamp != self.cached_stamp:
			self.cached_stamp = stamp
			print(stamp)
# Create Object to watch for File Change
fChng = Monkey()

# Specify the mmWave binary File path (the leading r is required)
binPath = r'C:\ti\mmwave_studio_02_01_01_00\mmWaveStudio\PostProc\adc_data_Raw_0.bin'

# Connect the Port For the 3D printer
ser = serial.Serial(port = "COM13", baudrate=115200)

# Specify the Measurement Locations
measLoc = np.array([[0,0,100],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]])

# Specify the Number of Times to go through the measurements
numLoop = 1

#Specify the mmWave Studio Measurement Button Pixel Location

# Do a 3D printer Calibration then send printer to home location
time.sleep(2)
ser.write(b'G28 W\r\n')


#Wait for 3D printer to finish calibrating
readSer=True
while readSer:
	a=ser.readline().decode('UTF-8')
	if a=="ok\n":
		readSer=False

#Tell 3D printer to use absolute coordinates
ser.write(b'G90\n')
while readSer:
	a=ser.readline().decode('UTF-8')
	if a=="ok\n":
		readSer=False

#Tell 3D printer to use absolute coordinates
ser.write(b'M203 Z80\n')
while readSer:
	a=ser.readline().decode('UTF-8')
	if a=="ok\n":
		readSer=False

#Move the 3D Printer to the initial Measurement Location
moveCom = 'G1 '+ 'X'+str(measLoc[0,0]) + ' Y'+str(measLoc[0,1]) + ' Z'+str(measLoc[0,2]) + ' E0' + ' F4800' + '\r\n'
print('moving to',moveCom)

ser.write(bytes(moveCom, 'utf-8'))

while readSer:
	a=ser.readline().decode('UTF-8')
	if a=="ok\n":
		readSer=False

## Take the First Measurement
mouse.position = (688,353)
mouse.click(Button.left,1)

mouse.position = (777,353)
mouse.click(Button.left,1)

while(True):
	fChng.ook()







