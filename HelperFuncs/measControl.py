import matlab.engine #Imports matlab runtime engine
import os #Used for file handling


class Measurement(object):
	def __init__(self):
		self.storPathPy = 'C:\\Users\\ColeHarlow\\Documents\\GitHub\\synthApertureTesting\\Measurements\\'
		self.storPathLua = 'C:\\\\Users\\\\ColeHarlow\\\\Documents\\\\GitHub\\\\synthApertureTesting\\\\Measurements\\\\'
		self.basename = 'ADCdata'
		self.mmAppend = '_Raw_0'
		self.ext = '.bin'
		self.radarMeasNum = 0
		self.eng = matlab.engine.start_matlab() #Initializes Matlab runtime engine

		#self.eng.TakeMeas()

		#Check that the storage path is a file
		if not os.path.isdir(self.storPathPy):
			os.mkdir(self.storPathPy) #if folders does not exist, create the folder

		#Checks The Highest Measurement Number Folder that Already exists
		iM = 0
		for f in os.scandir(self.storPathPy):
			if f.is_dir():
				if "Measurement" in f.name:
					fold = f.name
					num = int(fold.replace("Measurement",''))
					if num>iM:
						iM = num

		self.storPathPy = self.storPathPy + '\\Measurement'+str(iM+1) + '\\'
		self.storPathLua = self.storPathLua + '\\\\Measurement'+ str(iM+1) + '\\\\'
		os.mkdir(self.storPathPy)

		#Initialize NET framework used to communicate with Radar
		self.eng.addpath('C:\\Users\\ColeHarlow\\Documents\\GitHub\\synthApertureTesting\\HelperFuncs\\MatlabLua')
		self.initNET()

	def initNET(self):
		self.eng.TakeMeas(1,0)

	def takeMeasure(self):
		self.eng.TakeMeas(0, (self.storPathLua+self.basename+str(self.radarMeasNum)+self.ext))
		self.checkDone()
		self.radarMeasNum+=1

	def checkDone(self):
		#Check if the file was created
		path = self.storPathPy+self.basename+str(self.radarMeasNum)+self.mmAppend+self.ext
		print(path)
		if os.path.exists(path):
			while True:
				if os.path.getsize(path)>0:
					print("Measure Done")
					return 
		print('Path Does Not Exist')


		





