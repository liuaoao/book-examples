# Chapter 10: The State of Things
import random

class State():

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

class NoQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You insert a quarter.")
        self.gumballMachine.setHasQuarterState()

    def ejectQuarter(self):
        print("You haven't inserted a quarter.")

    def turnCrank(self):
        print("You turned, but there's no quarter.")

    def dispense(self):
        print("You need to pay first.")

class HasQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        self.randomWinner = random.choice([True] + [False for i in range(9)])

    def insertQuarter(self):
        print("You can't insert another quarter.")

    def ejectQuarter(self):
        print("Quarter returned.")
        self.gumballMachine.setNoQuarterState()

    def turnCrank(self):
        print("You turned...")
        if self.randomWinner and self.gumballMachine.count > 1:
            self.gumballMachine.getWinnerState()
        else:
            self.gumballMachine.setSoldState()

    def dispense(self):
        print("No gumball dispense.")

class SoldState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball.")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank.")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball...")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.count > 0:
            self.gumballMachine.setNoQuarterState()
        else:
            self.gumballMachine.setSoldOutState()

class SoldOutState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out.")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter.")

    def turnCrank(self):
        print("You turned, but there are no gumballs.")

    def dispense(self):
        print("No gumball dispensed!")

class WinnerState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Wrong message.")

    def ejectQuarter(self):
        print("Wrong message.")

    def turnCrank(self):
        print("Wrong message.")

    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter!")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.count > 0:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.count > 0:
                self.gumballMachine.setNoQuarterState()
            else:
                print("Ops! out of gumballs!")
                self.gumballMachine.soldOutState()
        else:
            self.gumballMachine.setSoldOutState()

class GumballMachine():

    def __init__(self, numberGumballs:int):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)

        self.state = self.soldOutState
        self.count = numberGumballs

        if self.count > 0:
            self.state = self.noQuarterState


    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def releaseBall(self):
        print('A gumball comes rolling out the slot...')
        if self.count > 0:
            self.count -= 1

    def refill(self, count):
        self.count = count
        self.setNoQuarterState()

    # def setState(self, state:State()):
    #     self.state = state

    def setHasQuarterState(self):
        self.state = self.hasQuarterState

    def setNoQuarterState(self):
        self.state = self.noQuarterState

    def setSoldOutState(self):
        self.state = self.soldOutState

    def setSoldState(self):
        self.state = self.soldState

    def getWinnerState(self):
        self.state = self.winnerState

if __name__ == '__main__':
    gumballMachine = GumballMachine(5)
    print(gumballMachine.count)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine.count)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine.count)

