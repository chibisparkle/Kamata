class Keyword:
    def __init__(self, name, weight):
        self.name = name
        self.weight = 0
        self.weight = weight

    def myfunc(self):
        print("Hello my name is " + self.name)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight