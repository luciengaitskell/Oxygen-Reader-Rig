import smbus
bus = smbus.SMBus(1)
DEVICE_ADDRESS = 0x29
#The BlueESC's I2c address
TEMP = 0x06
#The temperature's I2c register (it's 2 bytes 0x06 and 0x07)
print("The BlueESC's Temperature is:")
print(bus.read_word_data(DEVICE_ADDRESS,TEMP))
print("Probably not in a real unit...")
