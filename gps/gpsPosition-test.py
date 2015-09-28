import gpsPosition

thread=gpsPosition.gpsPosition("localhost",2947)

thread.start()
print "started"

print "\n\nLon:"
print thread.getLon()
print "\nLat:"
print thread.getLat()
print "\nLat,Lon:"
print thread.getLatLon()

"""while True:
#	print thread.distanceGot
#	print thread.report
#	print thread.elapsed_time
	print "\nLon:"
	print thread.lon
	print "\nLat:"
	print thread.lat
#	print thread.checked
"""
thread.close()
print "finished"
thread.exit()
