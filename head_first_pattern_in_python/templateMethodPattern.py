# Chapter 8: Encapsulating Algorithms
from abc import ABCMeta, abstractmethod

class CaffeineBeverage():
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass

    def boilWater(self):
        print('Boiling water.')

    def pourInCup(self):
        print('Pouring into cup.')

    # hook
    def customerWantsCondiments(self):
        return True

class Tea(CaffeineBeverage):

    def brew(self):
        print('Steeping the tea.')

    def addCondiments(self):
        print('Adding Lemon.')

class Coffe(CaffeineBeverage):

    def brew(self):
        print('Dripping Coffe through filter.')

    def addCondiments(self):
        print('Adding sugar and milk.')

    def getUserInput(self):
        answer = None
        while answer not in ['y', 'Y', 'n', 'N']:
            answer = input('Wound you like milk and sugar with you coffee (y/n)?')
            if answer in ['y', 'Y']:
                return True
            else:
                return False

    # hook
    def customerWantsCondiments(self):
        return self.getUserInput()

def BeverageTestDriver():
    tea = Tea()
    coffe = Coffe()

    tea.prepareRecipe()
    coffe.prepareRecipe()

if __name__ == '__main__':
    BeverageTestDriver()
