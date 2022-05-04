"""OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class"""

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
    print(isinstance(School_bus,Vehicle))