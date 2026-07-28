from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

# Child class
class Car(Vehicle):

    def start(self):
        print("Car starts with a key.")

# Another child class
class Bike(Vehicle):

    def start(self):
        print("Bike starts with a self-start button.")

# Creating objects
car = Car()
car.start()

bike = Bike()
bike.start()