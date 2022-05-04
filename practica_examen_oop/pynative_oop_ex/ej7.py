"""OOP Exercise 7: Check type of an object

Write a program to determine which class a given Bus object belongs to."""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        """_summary_

        Args:
            name (str): name of the vehicle
            mileage (int): int
            capacity (int): int
        """
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

if __name__ == "__main__":
    School_bus = Bus("School Volvo", 12, 50)
    print(type(School_bus))