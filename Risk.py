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
        self.riskFactors['doorOpen'] = Factor(10000, 1)
        self.riskFactors['windowOpen'] = Factor(10, 1)
        self.riskFactors['smokeAlarm'] = Factor(2, 1)

    def calculateRisk(self):
        risk = 0
        for i in self.riskFactors:
            risk += self.riskFactors[i].val*self.riskFactors[i].weight
        risk=10*(-1/(risk+1)+1)
        return risk

