import numpy as np
import pandas as pd

class PreMeas(object):
	def __init__(self,xStart,zStart,xSteps,zSteps,xSpace,zSpace,path):
		self.xStart = xStart
		self.zStart = zStart
		self.xSteps = xSteps
		self.zSteps = zSteps
		self.xSpace = xSpace
		self.zSpace = zSpace

		self.path = path
		self.measLocs = self.genPoints()

	def genPoints(self):
		xCoord = np.array((np.arange(0,(self.xSteps),1)*self.xSpace)+ self.xStart)
		zCoord = np.array((np.arange(0,(self.zSteps),1)*self.zSpace)+ self.zStart)

		measLocs = np.zeros((self.xSteps*self.zSteps,3))

		for iz,z in enumerate(zCoord):
			for ix,x in enumerate(xCoord):
				measLocs[iz*self.xSteps+ix,0] = x
				measLocs[iz*self.xSteps+ix,2] = z
		return(measLocs)

	def savePoints(self):
		df = pd.DataFrame(self.measLocs)
		fname = 'measLocs.xlsx'
		print(self.path+fname)
		df.to_excel(self.path+fname,index=False)




