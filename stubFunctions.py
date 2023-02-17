class StubCode:
    def __init__(self):
        self.callCountStubDataGenerator = 0
        self.callCountStubOutputFormatter = 0
        self.callCountStubPrintToConsole = 0
    def stubDataGenerator(self):
        self.callCountStubDataGenerator += 1
        return {'SOC':30,'T':35}

    def stubOutputFormatter(self,input_data):
        self.callStubOutputFormatter += 1
        return input_data
    
    def stubPrintToConsole(self,input_data):
        self.callCountStubPrintToConsole += 1
