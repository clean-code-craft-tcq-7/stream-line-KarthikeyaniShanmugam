import unittest
from stubFunctions import *
from SenderMain import *

class SenderMainTester(unittest.TestCase):
    def test(self):  
        stub = StubCode()
        sender = Sender(generator = stub ,formatterFunction = stub.stubOutputFormatter ,printerFunction = stub.stubPrintToConsole)
        sender.sendData()
        self.assertTrue(stub.callCountStubDataGenerator == 1)
        self.assertTrue(stub.callCountStubOutputFormatter == 1)
        self.assertTrue(stub.callCountStubDataGenerator == 1)
if __name__ == '__main__':
    unittest.main()