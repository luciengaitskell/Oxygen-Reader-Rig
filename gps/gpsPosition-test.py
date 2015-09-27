import gpsPosition

thread=gpsPosition.gpsPosition("localhost",2947)

thread.start()
print "started"
while True:
	print thread.report
#	print thread.elapsed_time
#	print thread.lon
#	print thread.checked
thread.close()
print "finished"
thread.exit()
