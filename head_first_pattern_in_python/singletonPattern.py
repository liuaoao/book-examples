# Chapter 5: Cho-O-holic

from threading import Thread
from time import sleep
import random

class ChocolateBoiler_before():

    def __init__(self):
        self.empty = True
        self.boiled = False


    def fill(self, thread_name):
        self.empty = False
        self.boiled = False
        sleep(random.randint(1,4))
        print(self)
        print('%s: Fill successfully, empty: %s, boiled: %s' %(thread_name, self.empty, self.boiled))

    def drain(self, thread_name):
        if not self.isEmpty() and self.isBoiled():
            self.empty = True
            sleep(random.randint(1, 4))
        print(self)
        print('%s: drain successfully, empty: %s, boiled: %s' %(thread_name, self.empty, self.boiled))

    def boil(self, thread_name):
        if not self.isEmpty() and not self.isBoiled():
            self.boiled = True
            sleep(random.randint(1, 4))
        print(self)
        print('%s: boil successfully, empty: %s, boiled: %s' %(thread_name, self.empty, self.boiled))

    def isEmpty(self):
        return self.empty

    def isBoiled(self):
        return self.boiled

_chocolate_boiler_instance = None


def make_chocolate_before(thread_name):
    boiler = ChocolateBoiler_before()
    boiler.fill(thread_name)
    boiler.boil(thread_name)
    boiler.drain(thread_name)

def make_chocolate_after(thread_name):
    global _chocolate_boiler_instance

    if _chocolate_boiler_instance == None:
        boiler = ChocolateBoiler_before()
        _chocolate_boiler_instance = boiler
    else:
        boiler = _chocolate_boiler_instance

    boiler.fill(thread_name)
    boiler.boil(thread_name)
    boiler.drain(thread_name)

class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        pass


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Cls4(metaclass=Singleton):
    pass



if __name__ == '__main__':
    # print("---- single thread test without Singleton Pattern ----")
    # make_chocolate_before('single thread')

    # print("\n ----- multi thread test without Singleton Pattern -----\n")
    #
    # thread1 = Thread(target=make_chocolate_before, args=('--- thread 1 ---', ))
    # thread2 = Thread(target=make_chocolate_before, args=('--- thread 2 ---', ))
    # thread3 = Thread(target=make_chocolate_before, args=('--- thread 3 ---', ))
    #
    # thread1.start()
    # thread2.start()
    # thread3.start()

    # print("\n ----- multi thread test with Singleton Pattern -----\n")
    # boiler = ChocolateBoiler_before()
    #
    # thread1 = Thread(target=make_chocolate_after, args=('--- thread 1 ---', ))
    # thread2 = Thread(target=make_chocolate_after, args=('--- thread 2 ---', ))
    # thread3 = Thread(target=make_chocolate_after, args=('--- thread 3 ---', ))
    #
    # thread1.start()
    # thread2.start()
    # thread3.start()

    print('using \'new\' to realize singleton')
    single1 = Single()
    single2 = Single()
    print(id(single1) == id(single2))

    print('using superclass to realize singleton.')
    cls1 = Cls4()
    cls2 = Cls4()
    print(id(cls1) == id(cls2))
