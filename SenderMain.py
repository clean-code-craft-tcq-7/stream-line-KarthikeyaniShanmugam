from ConsolePrinter import printToConsole
from DataGenerator import DataGenerator
from OutputFormatter import OutputFormatter
class Sender:
    def __init__(self,generator = DataGenerator ,formatter= OutputFormatter ,printerFunction = printToConsole):
        self.dataStreamCount = 50
        self.generator = generator
        self.formatter = formatter
        self.printerFunction = printerFunction
    def sendData(self):
        for i in range(0,self.dataStreamCount):
            generatedDict = self.generator.generateBatteryData()
            JsonString = self.formatter.formatOutput(generatedDict)
            self.printerFunction(JsonString.encode())
if __name__ == "__main__":
    sender = Sender()
    sender.sendData()