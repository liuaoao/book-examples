# Chapter 1: Mini Duck Simulator.
from abc import abstractmethod, ABC

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can not fly.")

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("MuteQuack")

class Squack(QuackBehavior):
    def quack(self):
        print("Squack")

class Duck(ABC):
    def __init__(self):
        self.flyBehavior = FlyBehavior()
        self.quackBehavior = QuackBehavior()

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def performSwim(self):
        print("All duck can swim!")

    def setFlybehavior(self, fb):
        self.flyBehavior = fb

    def setQuackBehavior(self, qb):
        self.quackBehavior = qb

class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Squack()

    def display(self):
        print("I'm a ModelDuck.")

class FlyRocketPower(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket.")

class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("I'm a Mallard Duck.")

if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.display()
    mallard.performFly()
    mallard.performQuack()
    mallard.setFlybehavior(FlyRocketPower())
    mallard.performFly()

    model = ModelDuck()
    model.display()
    model.performFly()
    model.performQuack()
    model.performSwim()