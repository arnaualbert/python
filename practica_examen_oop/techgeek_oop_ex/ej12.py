"""Python OOPs Exercise 11: Write a Python class Square, and define two methods that return the square area and perimeter."""

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*(self.side)


if __name__ == "__main__":
    #initialize the objects of Square class
    square1 = Square(10)
    square2 = Square(20)

    print("The Area of square1 is:", square1.area())
    print("The Perimeter of square1 is:", square1.perimeter())

    print("\n\nThe Area of square2 is:", square2.area())
    print("The Perimeter of square2 is:", square2.perimeter())