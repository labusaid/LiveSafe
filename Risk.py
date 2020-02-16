class Factor:
    def __init__ (self, val, weight):
        self.val = val
        self.weight = weight


class Risk:
# time in seconds?
# counts and days integer values
# waterPressureFactor ???
    riskFactors = dict()

    def __init__(self):
        self.riskFactors['doorOpen'] = Factor(0, 1)
        self.riskFactors['windowOpen'] = Factor(0, 0.5)
        self.riskFactors['smokeAlarm'] = Factor(0, 2)

    def calculateRisk(self):
        risk = 0
        for i in self.riskFactors:
            risk += self.riskFactors[i].val*self.riskFactors[i].weight
        risk=10*(-1/(risk/10+1)+1)
        return risk

    def set(self, timeCount, doorCount, smokeCount, windowCount):
        self.riskFactors['doorOpen'].val = doorCount
        self.riskFactors['windowOpen'].val = windowCount
        self.riskFactors['smokeAlarm'].val = smokeCount

