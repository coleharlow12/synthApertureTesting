import sys
import time

def setup(ser,max_XSpeed,max_ZSpeed):
	# Send Printer to home location
	time.sleep(2)
	ser.write(b'G28 W\r\n') #W is required to skip calibration
	checkOk(ser)

	#Tell 3D printer to use absolute coordinates
	ser.write(b'G90\n')
	checkOk(ser)

	ser.write(bytes('M203 X'+str(max_XSpeed)+' \n','utf-8')) #Set max X speed in mm/sec
	ser.write(bytes('M203 Z'+str(max_ZSpeed)+' \n','utf-8')) #Set max Z speed in mm/sec


def DoMove(ser,coords,xSpeed,zSpeed):
	moveComX = 'G1'+ ' X'+str(coords[0])+' E0'+' F'+str(60*xSpeed)+' \r\n'
	ser.write(bytes(moveComX, 'utf-8'))
	isDone(ser)
	moveComZ = 'G1'+ ' Z'+str(coords[2])+' E0'+' F'+str(60*xSpeed)+' \r\n'
	ser.write(bytes(moveComZ, 'utf-8'))
	isDone(ser)

#Ensures the printer sends an okay before moving to next command
def checkOk(ser):
	count = 0
	while True:
		a=ser.readline().decode('UTF-8')
		count+=1
		if a=="ok\n":
			return (1)
		if count > 50:
			sys.exit("Port Read Timed Out")

#First it checks that the move command responds with ok. Next
def isDone(ser):
	checkOk(ser)
	ser.write(b'M400\n') #Tells the printer to wait to finish the move before doing next task
	checkOk(ser)
	return(0)
