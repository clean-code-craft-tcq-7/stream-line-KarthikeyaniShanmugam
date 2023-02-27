import unittest
from stubFunctions import *
from SenderMain import *

class SenderMainTester(unittest.TestCase):
    def test(self):  
        stub = StubCode()
        sender = Sender(generatorFunction = stub.generateBatteryData ,formatterFunction = stub.formatOutput ,printerFunction = stub.stubPrintToConsole)
        sender.sendData()
        self.assertTrue(stub.callCountStubDataGenerator == 50)
        self.assertTrue(stub.callCountStubOutputFormatter == 50)
        self.assertTrue(stub.callCountStubDataGenerator == 50)
        print("callCountStubDataGenerator:",stub.callCountStubDataGenerator)
        print("callCountStubOutputFormatter:",stub.callCountStubOutputFormatter)
        print("callCountStubDataGenerator:",stub.callCountStubDataGenerator)
if __name__ == '__main__':
    unittest.main()