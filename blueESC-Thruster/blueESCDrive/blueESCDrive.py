import smbus
import threading
DEFAULT={'busNumb':1, 'address':0x29}
ADDRESSES={'throttle':0x00}

class blueESCDrive:
    def __init__(self, address=DEFAULT['address'], busNumb=DEFAULT['busNumb']):
        self.BUS = smbus.SMBus(busNumb)
        self.ADDRESS=address

    def IOByte(self, address, inputValue=None):
        returnVal = self.IO(False, address, inputValue)
        if not returnVal == None:
            return returnVal
    def IOWord(self, address, inputValue=None):
        returnVal = self.IO(True, address, inputValue)
        if not returnVal == None:
            return returnVal
    def IO(self, word, address, inputValue=None):
        if inputValue==None:
            if word:
                return self.BUS.read_word_data(self.ADDRESS, address)
            else:
                return self.BUS.read_byte_data(self.ADDRESS, address)
        else:
            if word:
                self.BUS.write_word_data(self.ADDRESS, address, inputValue)
            else:
                self.BUS.write_byte_data(self.ADDRESS, address, inputValue)

    def power(self, inputPower=None):
        if inputPower==None:
            return self.IOWord(ADDRESSES['throttle'])
        else:
            if not type(inputPower) is int:
                raise TypeError("inputPower requires 'int' not '" + type(inputPower).__name__ + "'")
            """if self.inputPower() == 0:
                self.IOWord(ADDRESSES['throttle'], 0)"""
            self.IOWord(ADDRESSES['throttle'], 0)
            self.IOWord(ADDRESSES['throttle'], inputPower)
