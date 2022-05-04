"""OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it."""

class Vehicle:

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

    def __init__(self, name, max_speed, mileage):
        """_summary_

        Args:
            name (str): the name of the vehicle
            max_speed (int): the maximum speed
            mileage (int): the mileage
        """
        super().__init__(name, max_speed, mileage)   



if __name__ == "__main__":

    School_bus = Bus("School Volvo",180,12)
    print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)