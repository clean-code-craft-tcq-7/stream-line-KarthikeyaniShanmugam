import json
class StubCode:
    def __init__(self):
        self.callCountStubDataGenerator = 0
        self.callCountStubOutputFormatter = 0
        self.callCountStubPrintToConsole = 0
    def generateBatteryData(self):
        self.callCountStubDataGenerator += 1
        return {'SOC':30,'T':35}

    def formatOutput(self,input_data):
        self.callCountStubOutputFormatter += 1
        return json.dumps(input_data)
    
    def stubPrintToConsole(self,input_data):
        self.callCountStubPrintToConsole += 1


