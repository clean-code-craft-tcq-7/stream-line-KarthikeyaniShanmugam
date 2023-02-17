import unittest
from stubFunctions import *
from SenderMain import *

class SenderMainTester(unittest.TestCase):
    def test(self):  
        stub = StubCode()
        sender = Sender()
        sender.sendData(generatorFunction = stub.stubDataGenerator() ,formatterFunction = stub.stubOutputFormatter ,printerFunction = stub.stubPrintToConsole)
        self.assertTrue(stub.callCountStubDataGenerator == 1)
        self.assertTrue(stub.callCountStubOutputFormatter == 1)
        self.assertTrue(stub.callCountStubDataGenerator == 1)
if __name__ == '__main__':
    unittest.main()