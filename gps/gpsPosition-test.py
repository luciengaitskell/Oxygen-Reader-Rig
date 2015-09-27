import gpsPosition

thread=gpsPosition.gpsPosition("localhost",2947)

thread.start()
print "started"
print thread.getLat()
thread.close()
print "finished"
thread.exit()
