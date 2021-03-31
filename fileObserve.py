import os

class Monkey(object):
	def __init__(self):
		self.cached_stamp=0
		self.filename= r'C:\Users\ColeHarlow\Documents\GitHub\synthApertureTesting\fileObserve.py'

	def ook(self):
		stamp = os.stat(self.filename).st_mtime
		if stamp != self.cached_stamp:
			self._cached_stamp = stamp
			print(stamp)


fChng = Monkey()

fChng.ook()

#fdffda