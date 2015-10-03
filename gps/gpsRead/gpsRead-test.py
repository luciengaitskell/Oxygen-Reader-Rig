import gpsRead

debug = False
thread=gpsRead.gpsRead("localhost",2947)
print "started"

print "\n\nLon:"
print thread.getLon()
print "\nLat:"
print thread.getLat()
print "\[nLat,Lon]:"
print thread.getLatLon()

if debug:
	while True:
		print "\n The GPS Report Dictionary:"
		print thread.report
		print "\nLon Var:"
		print thread.lon
		print "\nLat Var:"
		print thread.lat

thread.close()
print "finished"
thread.exit()
