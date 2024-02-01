class Temperature:
    def __init__(self):
        self.currTemp = 0.0
    
    def getTemperature(self):
        print(self.currTemp)
        return self.currTemp
    
    def setTemperature(self):
        inputs = float(input())
        self.currTemp = inputs
        print("Set temperature to: " + str(self.currTemp))

