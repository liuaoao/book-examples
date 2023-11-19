# Chapter 2: Weather Station.

import random
from abc import abstractmethod, ABCMeta

def getTemperature():
    # Temperature Measurement Simulator
    # return float
    return random.uniform(0.0, 40.9)

def getHumidity():
    # Humidity Measurement Simulator
    # return float
    return str(random.uniform(30, 50))

def getPressure():
    # Pressure Measurement Simulator
    # return float
    return str(random.uniform(180, 400))


class WeatherDataInAWrongWay():
    # A Wrong Example
    def measurementsChanged(self):
        temp = getTemperature()
        humidity = getHumidity()
        pressure = getPressure()

        # currentConditionsDisplay.update(temp, humidity, pressure)
        # statisticsDisplay.update(temp, humidity, pressure)
        # forecastDisplay.update(temp, humidity, pressure)
        # other display...

class Subject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def registerObserver(self, o):
        # Observer类型
        pass

    @abstractmethod
    def removeObserver(self, o):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, temp, humidify, pressure):
        pass

class Displayment(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        pass

class WeatherData(Subject):

    def __init__(self):
        self.__temperature = float
        self.__humidity = float
        self.__pressure = float
        self.observers = list()

    def registerObserver(self, o):
        self.observers.append(o)

    def removeObserver(self, o):
        self.observers.remove(o)

    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.__temperature, self.__humidity, self.__pressure)

    def measurementsChanged(self):
        self.notifyObserver()

    def setMeasurements(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementsChanged()

class CurrentConditionDisplay(Observer, Displayment):
    # this currentCondition is a Observer.
    def __init__(self):
        self.__temperature = float
        self.__humidity = float
        self.__pressure = float
        self.weatherData = Subject()

    def CurrentConditionDisplay(self, weatherData):
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp, humidify, pressure):
        self.__temperature = temp
        self.__humidity = humidify
        self.__pressure = pressure

    def display(self):
        print("Current Condition: %s degress and humidity %s and pressure %s" %(self.__temperature,
                                                                                self.__humidity,
                                                                                self.__pressure))

if __name__ == '__main__':
    weatherData = WeatherData()
    currentDisplay = CurrentConditionDisplay()
    # Observer registered to the weatherData
    currentDisplay.CurrentConditionDisplay(weatherData)
    # bulid more display(observer)...

    # Once the weather data has been set, the boardcast(display) will be updated.
    weatherData.setMeasurements(getTemperature(), getHumidity(), getPressure())
    currentDisplay.display()