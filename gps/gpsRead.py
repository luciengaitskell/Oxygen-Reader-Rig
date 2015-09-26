import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	report=session.next
	if report['class'] == 'TPV':
		print(report)
"""
print(session.waiting)
print("Direct read:")
print(session.read)
print("\nWait for new input read:")
print(session.data)
print("\n\n")
"""
session.close()

