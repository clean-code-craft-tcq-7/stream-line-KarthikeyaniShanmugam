from ConsolePrinter import printToConsole
from DataGenerator import DataGenerator
from OutputFormatter import OutputFormatter
class Sender:
    def __init__(self,generatorFunction = DataGenerator.generateBatteryData,formatterFunction= OutputFormatter.formatOutput,printerFunction=printToConsole):
        self.dataStreamCount = 50
        self.generatorFunction = generatorFunction
        self.formatterFuntion = formatterFunction
        self.printerFunction = printerFunction
    def sendData(self):
        for i in range(0,self.dataStreamCount):
            generatedDict = self.generatorFunction()
            JsonString = self.formatterFuntion(generatedDict)
            self.printerFunction(JsonString.encode())
if __name__ == "__main__":
    sender = Sender()
    sender.sendData(generatorFunction = DataGenerator.generateBatteryData,formatterFunction= OutputFormatter.formatOutput,printerFunction=printToConsole)