# Chapter 3: Starbuzz Coffee.

from abc import ABCMeta, abstractmethod

# all beverage base class
class Beverage():
    __metaclass__ = ABCMeta

    description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass

# condiment abstract class
class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getDescription(self):
        pass

# here to write coffee
class Espresso(Beverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):

    def __init__(self):
        self.description = "HouseBlend"

    def cost(self):
        return 0.89

class DarkRoast(Beverage):

    def __init__(self):
        self.description = "DarkRoast"

    def cost(self):
        return 0.99

class DeCaff(Beverage):

    def __init__(self):
        self.description = "DeCaff"

    def cost(self):
        return 1.05

# here to write comdiment
class Mocha(CondimentDecorator):

    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()

class Milk(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"

    def cost(self):
        return 0.10 + self.beverage.cost()

class Soy(CondimentDecorator):
    beverage = Beverage()

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"

    def cost(self):
        return 0.10 + self.beverage.cost()

class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return 0.15 + self.beverage.cost()

if __name__ == "__main__":
    beverage = Espresso()
    print(beverage.getDescription(), " $", beverage.cost())

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.getDescription(), " $", beverage2.cost())

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.getDescription(), " $", beverage3.cost())