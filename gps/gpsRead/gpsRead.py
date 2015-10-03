import gps
import threading
import time

class gpsRead(threading.Thread):
	def __init__(self, host, port):
		super(gpsRead, self).__init__()
		self.session = gps.gps(host, port)
		self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
		self.stop=False
		self.defaultValue="waiting for a value..."
		self.lon=self.defaultValue
		self.lat=self.defaultValue
		self.report="not set yet"
		threading.Thread.start(self)


	def check(self):
		self.report = self.session.next()

		if self.report['class'] == 'TPV':
			if hasattr(self.report,"lon"):
				self.lon = self.report['lon']
			if hasattr(self.report,"lat"):
				self.lat = self.report['lat']

	def run(self):
		while not self.stop:
			self.check()
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
