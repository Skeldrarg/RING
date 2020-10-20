import random
import math

class Perso:

    def __init__(self):
        self.name = input("Name : ")
        self.FOR = math.inf
        self.DEX = math.inf
        self.INT = math.inf
        self.CON = math.inf
        self.EXP = 1
        self.MIN_EXP = 1
        self.MAX_EXP = 20
        self.PV = 0
        self.CAPACITES = []

    def __repr__(self):
        repr = "{name} the {TYPE}\n\nFOR | {0}\nDEX | {1}\nINT | {2}\nCON | {3}\n----+----\nEXP | {4}\n----+----\nPV  | {5}".\
                format(self.FOR,self.DEX,self.INT,self.CON,self.EXP,self.PV,name=self.name, TYPE=self.TYPE)
        if len(self.CAPACITES) > 0:
            repr += "\n\nCapacités : \n"
            for capacite in self.CAPACITES:
                repr += "{0}\n".format(capacite.TYPE)
        return repr

    def setVitality(self):
        self.PV = 200-(self.FOR + self.DEX + self.INT + self.CON) + self.EXP*3

class Warrior(Perso):

    def __init__(self):
        super().__init__()
        self.TYPE = "Warrior"

    def setStats(self):
        while (self.FOR + self.DEX + self.INT + self.CON > 100 + self.EXP)\
        or (self.FOR < self.DEX + 10)\
        or (self.DEX < self.INT + 10)\
        or (self.INT < self.CON):
            self.FOR = random.randint(1, 100)
            self.DEX = random.randint(1, 100)
            self.INT = random.randint(1, 100)
            self.CON = random.randint(1, 100)

    def setVitality(self):
        super().setVitality()

class Mage(Perso):

    def __init__(self):
        super().__init__()
        self.TYPE = "Mage"

    def setStats(self):
        while (self.FOR + self.DEX + self.INT + self.CON > 100 + self.EXP)\
        or (self.INT < max(self.FOR, self.DEX) + 15)\
        or (self.CON < max(self.FOR, self.DEX) + 15):
            self.FOR = random.randint(1, 100)
            self.DEX = random.randint(1, 100)
            self.INT = random.randint(1, 100)
            self.CON = random.randint(1, 100)

class Thief(Perso):

    def __init__(self):
        super().__init__()
        self.TYPE = "Thief"

    def setStats(self):
        while (self.FOR + self.DEX + self.INT + self.CON > 100 + self.EXP):
            self.FOR = random.randint(20, 100)
            self.DEX = random.randint(20, 100)
            self.INT = random.randint(20, 100)
            self.CON = random.randint(20, 100)