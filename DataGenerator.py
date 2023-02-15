import random
class DataGenerator:
    def __init__(self):
        self.socMin = 0
        self.socMax = 100
        self.tMin = -20
        self.tMax = 45
    def generateBatteryData(self):
        dataDict = {}
        dataDict['SOC'] = random.randint(self.socMin, self.socMax+1)
        dataDict['T'] = random.randint(self.tMin, self.tMax+1)
        return dataDict

if __name__ == "__main__":
    gen = DataGenerator()
    print(gen.generateBatteryData()['SOC'] in range(gen.socMin,gen.socMax+1))
    print(gen.generateBatteryData()['T'] in range(gen.tMin,gen.tMax+1))