import gps
import threading
import time

class gpsPosition(threading.Thread):
	def __init__(self, host, port):
		super(gpsPosition, self).__init__()
		self.session = gps.gps("localhost", "2947")
		self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
		self.stop=False
		self.lon="init"
		self.lat="inti"
		self.elapsed_time=0
		self.checked=False
		self.report="not set yet"


	def check(self):
		self.report = self.session.next()

		if self.report['class'] == 'TPV':
			if hasattr(self.report,self.lon):
				self.lon = self.report['lon']
			if hasattr(self.report,self.lat):
				self.lat = self.report['lat']

	def run(self):
		startTime=time.time()
		self.elapsed_time = 0
		while self.elapsed_time < 5:
			self.elapsed_time = time.time() - startTime

		while not self.stop:
			self.check()
			self.checked=True
		print("finished")

	def getLatLon(self):
		while not self.lon == "" and not self.lat == "":
			pass
		return [self.lon,self.lan]
	def getLon(self):
		return (self.getLatLon())[0]
	def getLat(self):
		return (self.getLatLon())[1]
	def getElTime(self):
		return self.elapsed_time
	def close(self):
		self.stop=True
		quit()
