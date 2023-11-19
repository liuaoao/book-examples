# Chapter 9: Well-Managed Collections

import itertools

class MenuItem():

    def __int__(self, name:str, description:str, vegetarian:bool, price:float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def isVegetarian(self):
        return self.vegetarian

class PancakeHouseMenu():

    def __init__(self):
        self.menuItems = []

        self.addItem(
            'K&B\'s Pancake Breakfast',
            'Pancake with scrambled eggs, and toast',
            True,
            2.99
        )
        self.addItem(
            'Regular Pancake Breakfast',
            'Pancakes with fried eggs, sausage',
            True,
            3.59
        )
        self.addItem(
            'Blueberries Pancakes',
            'Pancake made with fresh blueberries',
            True,
            3.59
        )
        self.addItem(
            'Waffles',
            'Waffles, with your choice of blueberries or strawberries',
            True,
            3.59
        )

    def addItem(self, name:str, description:str, vegetarian:bool, price:float):
        self.menuItems.append(
            MenuItem(name, description, vegetarian, price)
        )

    def getMenuIterms(self):
        return self.menuItems
    # other methods

class DinerMenu():

    def __init__(self):
        self.MAX_ITEMS = 6
        self.numberOfItem = 0
        self.menuItems = [None] * self.MAX_ITEMS

        self.addItem(
            'Vagetarian BLT',
            '(Fakin\') Bacon with lettuce & tomato on whole wheat',
            True,
            2.99
        )
        self.addItem(
            'BLT',
            'Bacon with lettuce & tomato on whole wheat',
            False,
            2.99
        )
        self.addItem(
            'Soup of the day',
            'Soup of the day, with a side of potato salad',
            False,
            3.29
        )
        self.addItem(
            'Hotdog',
            'A hot dog, with saurkraut, relish, onions, topped with cheese',
            False,
            3.05
        )

    def addItem(self, name:str, description:str, vegetarian:bool, price:float):
        if self.numberOfItem >= self.MAX_ITEMS:
            print('Sorry, menu is full! Can\'t add item to menu')
        else:
            self.menuItems[self.numberOfItem] = MenuItem(name, description, vegetarian, price)
            self.numberOfItem += 1

    def getMenuIterms(self):
        return self.menuItems
    # other methods