# Chapter 4: Pizza Test Diver.

from abc import ABCMeta, abstractmethod

# 产品类
class Pizza():
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = "normal pizza"
        self.dough = "normal dough"
        self.sauce = "normal sauce"
        self.toppings = []

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough... ")
        print("Adding sauce...")
        print("Adding Toppings" + str(self.toppings))

    def bake(self):
        print("Bake for 25 minutes at 350.")

    def cut(self):
        print("Cutting the pizza into diagonal slices.")

    def box(self):
        print("Place pizza in official PizzaStore box.")

    def getName(self):
        return self.name

class NYStyleCheesePizza(Pizza):

    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese"]

class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices.")

# 创建者类
class PizzaStore():
    __metaclass__ = ABCMeta

    @abstractmethod
    def createPizza(self, type):
        return Pizza()

    def orderPizza(self, type):

        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

class NYPizzaStore(PizzaStore):

    def createPizza(self, type):
        if type == "cheese":
            return NYStyleCheesePizza()
        elif type == "veggie":
            # haven't write NY style veggie class yet. please wait.
            return None
        elif type == "clam":
            # haven't write it yet
            return None
        elif type == "pepperoni":
            # haven't write it yet
            return None
        else:
            return None

class CaliforniaPizzaStore(PizzaStore):
    def createPizza(self, type):
        # haven't write it yet
        return None

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, type):
        if type == "cheese":
            return ChicagoStyleCheesePizza()
        # haven't write it yet
        return None

if __name__ == '__main__':
    # define a creator
    nyStore = NYPizzaStore()
    # choose a factory ( there is multiple factory )
    pizza = nyStore.orderPizza("cheese")
    # execute
    print("Customer have ordered a " +  pizza.getName())

    ccgStore = ChicagoPizzaStore()
    pizza = ccgStore.orderPizza("cheese")
    print("Customer have ordered a " +  pizza.getName())
