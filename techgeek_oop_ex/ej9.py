"""Python OOPs Exercise 9: Write a Python program that lists out all the default as well as custom properties of the class."""

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    teacher = Teacher("Lokesh", 36)
    print("Teacher class's object  all properties")

    print(dir(teacher))