import gps
import threading

class gpsPosition(threading.Thread):
	def __init__(self, host, port):
		super(gpsPosition, self).__init__()
		self.session = gps.gps("localhost", "2947")
		self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
		self.stop=False
		self.lon=0
		self.lat=0
	
	def run(self):
		#getting all of the previous iterations done
		while True:
			try:
				self.session.next()
			except StopIteration:
				break
		while not self.stop:
			self.report = self.session.next()
			
			if report['class'] == 'TPV':
				self.lon = self.report['lon']
				self.lat = self.report['lat']
		print("finished")
	
	def getLon(self):
		return self.lon
	def getLat(self):
		return self.lat

	def close(self):
		self.stop=True
		quit()
