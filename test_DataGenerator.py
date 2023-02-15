import unittest

from src import DataGenerator


class generateTester(unittest.TestCase):
    def test(self):  
        gen = DataGenerator.DataGenerator()
        self.assertTrue(gen.generateBatteryData()['SOC'] in range(gen.socMin,gen.socMax+1))
        self.assertTrue(gen.generateBatteryData()['T'] in range(gen.tMin,gen.tMax+1))
if __name__ == '__main__':
    unittest.main()