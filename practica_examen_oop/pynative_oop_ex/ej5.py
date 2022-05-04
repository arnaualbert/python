"""OOP Exercise 5: Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise."""

class Vehicle:
    """default color white
    """
    color="White"

    def __init__(self, name, max_speed, mileage):
        """_summary_

        Args:
            name (str): the name of the vehicle
            max_speed (int): the maximum speed
            mileage (int): the mileage
        """
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage



class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

if __name__ == "__main__":
    School_bus = Bus("School Volvo", 180, 12)
    print("color:",School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

    car = Car("Audi Q5", 240, 18)
    print("color:", car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)