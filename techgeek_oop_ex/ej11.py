"""Python OOPs Exercise 11: Write a program that prints the class name using its object."""

class Animal:
    pass

if __name__ == "__main__":

    # Animal class object
    lion = Animal()

    print("The ClassName of the lion object is: ", lion.__class__.__name__)