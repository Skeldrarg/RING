import random

class Capacite:

    def __init__(self,TYPE,*attrs):
        self.TYPE = TYPE
        for attr in attrs:
            exec("self.{0} = 0".format(attr))

    def setStats(self):
        while sum(list(self.__dict__.values())[1:]) != 100:
            #print(sum(list(self.__dict__.values())[1:]))
            i = 1
            while i < len(list(self.__dict__.keys())):
                setattr(self, list(self.__dict__.keys())[i],random.randint(20,100))
                i += 1

    def __repr__(self):
        return str(self.__dict__)