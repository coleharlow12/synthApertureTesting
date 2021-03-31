import os

class Monkey(object):
	def __init__(self):
		self.filename= r'C:\ti\mmwave_studio_02_01_01_00\mmWaveStudio\PostProc\adc_data_Raw_0.bin'
		self.cached_stamp= os.stat(self.filename).st_mtime

	def ook(self):
		stamp = os.stat(self.filename).st_mtime
		if stamp != self.cached_stamp:
			self.cached_stamp = stamp
			print(stamp)


fChng = Monkey()

fChng.ook()
print(fChng.cached_stamp)

while(True):
	fChng.ook()

#fdffda