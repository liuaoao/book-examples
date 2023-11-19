# Chapter 7: Being Adaptive

class Duck():

    def quark(self):
        pass

    def fly(self):
        pass

class MallardDuck():

    def quark(self):
        print('Quack')

    def fly(self):
        print('I am flying')

class Turkey():

    def gobble(self):
        pass

    def fly(self):
        pass

class WildTurkey(Turkey):

    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print('I am flying a short distance')

class TurkayAdapter(Turkey, Duck):

    def __init__(self, turkey):
        self.turkey = turkey

    def quark(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()

def DuckTestDriver():
    duck = MallardDuck()
    turkey = WildTurkey()

    turkeyAdapter = TurkayAdapter(turkey)

    print('The turkey says:')
    turkey.gobble()
    turkey.fly()

    def testDuck(duck):
        duck.quark()
        duck.fly()

    print('\nThe duck says:')
    testDuck(duck)

    print('\nThe TurkeyAdapter says:')
    testDuck(turkeyAdapter)

if __name__ == '__main__':
    DuckTestDriver()