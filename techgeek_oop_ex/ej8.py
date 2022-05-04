"""Python OOPs Exercise 8: Write a Python program that checks if one class is a subclass of another?"""


class Staff:
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

# inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    print("Is Teacher a subclass of Staff:", issubclass(Teacher, Staff))
    print("Is Staff a subclass of Teacher:", issubclass(Staff, Teacher))