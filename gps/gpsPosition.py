import gps
import threading
import time

class gpsPosition(threading.Thread):
	def __init__(self, host, port):
		super(gpsPosition, self).__init__()
		self.session = gps.gps("localhost", "2947")
		self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
		self.stop=False
		self.defaultValue="waiting for a value..."
		self.lon=self.defaultValue
		self.lat=self.defaultValue
		self.elapsed_time=0
		self.checked=False
		self.report="not set yet"
		self.distanceGot="hasn't been used yet"


	def check(self):
		self.report = self.session.next()
		presetDist="no where"

		if self.report['class'] == 'TPV':
			presetDist="class check"
			if hasattr(self.report,"lon"):
				presetDist="got to lon"
				self.lon = self.report['lon']
			if hasattr(self.report,"lat"):
				self.lat = self.report['lat']
		self.distanceGot=presetDist

	def run(self):
		"""startTime=time.time()
		self.elapsed_time = 0
		while self.elapsed_time < 5:
			self.elapsed_time = time.time() - startTime"""
		#NOT NEEDED: as the below functions wait for the lon/lat being set 

		while not self.stop:
			self.check()
			self.checked=True
		print("finished")

	def getLatLon(self):
		while not self.isReadReady():
			pass
		return [self.lat,self.lon]
	def getLon(self):
		return (self.getLatLon())[1]
	def getLat(self):
		return (self.getLatLon())[0]
	def isReadReady(self):
		if self.lon == self.defaultValue or self.lat == self.defaultValue:
			return False
		else:
			return True
	def close(self):
		self.stop=True
		quit()
