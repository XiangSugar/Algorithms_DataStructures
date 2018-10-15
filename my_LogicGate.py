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
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLable() + " --> "))
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLable() + " --> "))
        else:
            return self.pinB.getFrom().getOutput()
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error:NO EMPTY PINS!")

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLable() + " --> "))
        else:
            return self.pin.getFrom().getOutput()

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

class Connector(object):
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate
            
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

g4.getOutput()


# This program is not done
        