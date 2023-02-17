from ConsolePrinter import printToConsole
from DataGenerator import DataGenerator
from OutputFormatter import OutputFormatter
class Sender:
    def __init__(self):
        self.dataStreamCount = 50
    def sendData(self):
        generator = DataGenerator()
        formatter = OutputFormatter()
        for i in range(0,self.dataStreamCount):
            generatedDict = generator.generateBatteryData()
            JsonString = formatter.formatOutput(generatedDict)
            printToConsole(JsonString.encode())
if __name__ == "__main__":
    sender = Sender()
    sender.sendData()