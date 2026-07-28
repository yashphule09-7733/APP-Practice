class Car:
    def drive(self):
        print("Driving Car")

class Bike:
    def drive(self):
        print("Riding Bike")

vehicle_type = input("Enter vehicle (car/bike): ")

if vehicle_type == "car":
    vehicle = Car()
elif vehicle_type == "bike":
    vehicle = Bike()

vehicle.drive()