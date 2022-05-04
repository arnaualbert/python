class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

if __name__ == "__main__":
    School_bus = Bus("School Volvo", 12, 50)
    print(type(School_bus))