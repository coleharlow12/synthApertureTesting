import os
import time
import serial
import pdb
import numpy as np

from HelperFuncs.printerHelp import setup,DoMove
from HelperFuncs.measControl import Measurement
from HelperFuncs.preMeasure import PreMeas

# Connect the Port For the 3D printer
ser = serial.Serial(port = "COM3", baudrate=115200)
maxX = 25 #mm/s
maxZ = 25 #mm/s

start=np.array([[5, 30],[170,30]])
print(start[0][0])

#pdb.set_trace()

#Setup the printer
setup(ser,maxX,maxZ)

# Create the Measurement Object
Meas = Measurement()

# Specify the Measurement Locations
mLocs = PreMeas(xStart=start[0][0],zStart=start[0][1],xSteps=8,zSteps=16,xSpace=5,zSpace=2.5,path=Meas.storPathPy)
mLocs.genPoints()
mLocs.savePoints()

for coordIn in range(0,(mLocs.measLocs.shape[0])):
	# Move to the First Measurement Location
	DoMove(ser=ser,coords=mLocs.measLocs[coordIn,:],xSpeed=maxX,zSpeed=maxZ)
	time.sleep(0)
	#Meas.takeMeasure()

Meas1 = Measurement(initMat=False)

# Specify the Measurement Locations
mLocs = PreMeas(xStart=start[1][0],zStart=start[1][1],xSteps=8,zSteps=16,xSpace=5,zSpace=2.5,path=Meas1.storPathPy)
mLocs.genPoints()
mLocs.savePoints()

for coordIn in range(0,(mLocs.measLocs.shape[0])):
	# Move to the First Measurement Location
	DoMove(ser=ser,coords=mLocs.measLocs[coordIn,:],xSpeed=maxX,zSpeed=maxZ)
	time.sleep(0)
	#Meas1.takeMeasure()
