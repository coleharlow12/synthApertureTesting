import os
import time
import serial

from HelperFuncs.printerHelp import setup,DoMove
from HelperFuncs.measControl import Measurement
from HelperFuncs.preMeasure import PreMeas

# Connect the Port For the 3D printer
ser = serial.Serial(port = "COM3", baudrate=115200)
maxX = 50 #mm/s
maxZ = 50 #mm/s

#Setup the printer
setup(ser,maxX,maxZ)

# Create the Measurement Object
Meas = Measurement()

# Specify the Measurement Locations
mLocs = PreMeas(xStart=5,zStart=80,xSteps=8,zSteps=8,xSpace=2.5,zSpace=2.5,path=Meas.storPathPy)
mLocs.genPoints()
mLocs.savePoints()

for coordIn in range(0,(mLocs.measLocs.shape[0])):
	# Move to the First Measurement Location
	DoMove(ser=ser,coords=mLocs.measLocs[coordIn,:],xSpeed=maxX,zSpeed=maxZ)
	time.sleep(3)
	Meas.takeMeasure()








