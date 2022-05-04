"""OOP Exercise 4: Class Inheritance

Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class."""

class Vehicle:
    """this is a vehicle"""
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    """this is a child class of a vehicle called Bus"""
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

if __name__ == "__main__":

    School_bus = Bus("School Volvo", 180, 12)
    print(School_bus.seating_capacity())