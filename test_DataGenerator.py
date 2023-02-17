import unittest

from DataGenerator import *


class generateTester(unittest.TestCase):
    def test(self):  
        gen = DataGenerator()
        output = gen.generateBatteryData()
        self.assertTrue(output['SOC'] in range(gen.socMin,gen.socMax+1) and output['T'] in range(gen.tMin,gen.tMax+1))
if __name__ == '__main__':
    unittest.main()