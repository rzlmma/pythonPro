# -*- coding:utf-8 -*-
# __author__ = majing
"""
观察者模式 在对象之间定义了一对多的依赖，这样一来，当一个对象的状态发生了变化，依赖它的对象都会收到通知，并自动更新

《head first 设计模式》中的观察者模式 python实现
"""


class Subject(object):

    def register_observer(self, observer):
        raise NotImplementedError()

    def remove_observer(self, observer):
        raise NotImplementedError()

    def notify_observers(self):
        raise NotImplementedError()


class WeatherData(Subject):
    observers = []
    temperature = 0.0
    humidity = 0.0
    pressure = 0.0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class Observer(object):
    temperature = 0.0
    humidity = 0.0
    weatherData = None
    pressure = 0.0

    def update(self, temperature, humidity, pressure):
        raise NotImplementedError()

    def display(self):
        raise NotImplementedError()


class CurrentConditionsDisplay(Observer):

    def current_conditions_display(self, weatherData):
        self.weatherData = weatherData
        self.weatherData.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity")


if __name__ == "__main__":
    weatherData = WeatherData()
    display = CurrentConditionsDisplay()
    display.current_conditions_display(weatherData)

    weatherData.set_measurements(18, 10.1, 12)

    weatherData.set_measurements(17, 9.2, 12)



