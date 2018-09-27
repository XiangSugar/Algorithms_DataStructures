# coding  = utf-8
# 2018-9-25  20:54

class LogicGate(object):
    def __init__(self, n):
        self.lable =  n
        self.output = None
    def getLable(self):
        return self.lable
    def getOutput(self):
        self.output = self.performLogicGate()  #this function will be defined in the subclass
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        return int(input("Enter Pin A input for gate " + self.getLable() + " --> "))
    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLable() + " --> "))

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None
    def getPin(self):
        return int(input("Enter Pin input for gate " + self.getLable() + " --> "))

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    def performLogicGate(self):
        a = self.getPinA()
        b = self.getPinB()
        if 1 == a and 1== b:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    def performLogicGate(self):
        a = self.getPinA()
        b =self.getPinB()
        if 0 == a and 0 == b:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    def performLogicGate(self):
        pin = self.getPin()
        if 1 == pin:
            return 0
        else:
            return 1

g1 = AndGate("G1")
print(g1.getOutput())

g2 = OrGate("G2")
print(g2.getOutput())

g3 = NotGate("G3")
print(g3.getOutput())
        