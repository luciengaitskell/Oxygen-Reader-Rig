import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
    	report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print report
	print report['class']
	#prints the class value in the dictionary

	print report
	#prints the dictionary report

	if report['class'] == 'TPV':
		print report['lon']
		#read the lon value in the report dictionary
		#report.lon can be used too
    except KeyError:
		#catch errors
		pass
    except KeyboardInterrupt:
		#quits with keyboard interrupt
		session.close()
		quit()
		# quit() seems to stop error when using control c
    except StopIteration:
		session.close()
		print "GPSD has terminated"
