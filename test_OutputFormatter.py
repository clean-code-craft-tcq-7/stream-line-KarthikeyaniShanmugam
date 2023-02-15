import unittest
import json
from OutputFormatter import *

class generateTester(unittest.TestCase):
    # function to check for JSON String validity
    def is_valid(self,json_string):
        print("JSON String:", json_string)
        try:
            json.loads(json_string)
            return True
        except:
            return False
    def test(self):  
        outFormatter = OutputFormatter.OutputFormatter()
        self.assertTrue(self.is_valid(outFormatter.formatOutput({'SOC':20,'T':-1})))
if __name__ == '__main__':
    unittest.main()