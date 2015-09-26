import smbus
import time
bus = smbus.SMBus(1)
DEVICE_ADDRESS = 0x29
THROTTLE = 0x00
TEMP = 0x06
bus.write_byte_data(DEVICE_ADDRESS, THROTTLE, 10000)
time.sleep(1)
bus.read_byte_data(DEVICE_ADDRESS,TEMP)
bus.write_byte_data(DEVICE_ADDRESS, THROTTLE, 0)
