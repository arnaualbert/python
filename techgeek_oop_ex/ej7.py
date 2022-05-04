"""Python OOPs Exercise 7: Write a Python program that overloads the operator + and > for a custom class."""

class Orders:
    def __init__(self, items):
        self.items = items

    # overload the + operator
    def __add__(self, other):
        return self.items + other.items

    # overload the > operator
    def __gt__(self, other):
        return len(self.items) > len(other.items)



if __name__ == "__main__":
    order1 = Orders([1, 2, 3, 4, 5, 6])

    order2 = Orders([10, 20, 30])

    print("order1 + order2=", order1 + order2)
    print("order1 > order2=", order1 > order2)