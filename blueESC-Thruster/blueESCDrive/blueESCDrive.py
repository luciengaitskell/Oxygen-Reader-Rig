import smbus
DEFAULT={'busNumb':1, 'address':0x29}
ADDRESSES={'throttle':0x00}

class gpsRead(threading.Thread):
    def __init__(self, address=default.address, busNumb=default.busNumb):
        self.BUS = smbus.SMBus(busNumb)
        self.ADDRESS=address
    def run():
        pass
    def IOWord(self, address, inputValue=None):
        if inputValue==None:
            self.BUS.read_byte_data(self.ADDRESS, address)
        else:
            self.BUS.write_word_data(self.ADDRESS, address, importValue)

    def power(self, power=None):
        if power==None:
            return self.BUS.IOWord(self.ADDRESSES.throttle)
        else:
            if not type(power) is int:
                raise TypeError("(setPower) power requires 'int' not '" + type(power).__name__ + "'")
            if self.getPower() == 0
                self.IOWord(ADDRESSES.throttle, 0)
            self.IOWord(ADDRESSES.throttle, power)
