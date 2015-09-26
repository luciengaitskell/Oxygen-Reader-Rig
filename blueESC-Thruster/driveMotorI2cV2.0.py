import smbus
import time
bus = smbus.SMBus(1)
# you may have to use "SMBus(0)" for older pi's
DEVICE_ADDRESS = 0x29
# I2c address of the motor "0x29" is the default
THROTTLE = 0x00
# I2c register of the throttle (it is 16 bit/2 byte so treat it like a "word")
bus.write_word_data(DEVICE_ADDRESS, THROTTLE, 0)
bus.write_word_data(DEVICE_ADDRESS, THROTTLE, 10)
time.sleep(5)
print("the motor has stopped due to inactivity")
time.sleep(3)
print("starting...")
bus.write_word_data(DEVICE_ADDRESS, THROTTLE, 0)
bus.write_word_data(DEVICE_ADDRESS, THROTTLE, -10)
time.sleep(4)
print("reversing...")
bus.write_word_data(DEVICE_ADDRESS, THROTTLE, 10)
time.sleep(8)
print("attempting to start without initialization")
bus.write_word_data(DEVICE_ADDRESS, THROTTLE, 10)
print("It shouldn't drive")
