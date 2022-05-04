"""OOP Exercise 1: Create a Class with instance attributes

Write a Python program to create a Vehicle class with max_speed and mileage instance attributes."""


class Vehicle():
    """This is a vehicle"""

    def __init__(self,max_speed: int,mileage: int) -> None:
        self.max_speed = max_speed
        self.mileage = mileage

if __name__ == "__main__":
    modelX = Vehicle(240,18)
    print(modelX.max_speed, modelX.mileage)