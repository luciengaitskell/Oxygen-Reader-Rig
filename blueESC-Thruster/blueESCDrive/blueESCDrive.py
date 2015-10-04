import smbus
import threading
DEFAULT={'busNumb':1, 'address':0x29}
ADDRESSES={'throttle':0x00}

class blueESCDrive(threading.Thread):
    def __init__(self, address=DEFAULT['address'], busNumb=DEFAULT['busNumb']):
        self.BUS = smbus.SMBus(busNumb)
        self.ADDRESS=address
    def run():
        pass
    def IOWord(self, address, inputValue=None):
        if inputValue==None:
            return self.BUS.read_byte_data(self.ADDRESS, address)
        else:
            self.BUS.write_word_data(self.ADDRESS, address, inputValue)

    def power(self, power=None):
        if power==None:
            return self.IOWord(ADDRESSES['throttle'])
        else:
            if not type(power) is int:
                raise TypeError("(setPower) power requires 'int' not '" + type(power).__name__ + "'")
            """if self.power() == 0:
                self.IOWord(ADDRESSES['throttle'], 0)"""
            self.IOWord(ADDRESSES['throttle'], power)
