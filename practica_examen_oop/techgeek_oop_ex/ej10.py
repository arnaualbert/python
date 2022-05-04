"""Python OOPs Exercise 10: Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method. """





class Stack:
    # initialize an empty list
    def __init__(self):
        # conventional private member
        self.__stack = []

    # add items to the stack
    def push(self, item):
        self.__stack.append(item)

    # pop item from the stack
    def pop(self):
        self.__stack.pop()

    def traverse(self):
        for item in self.__stack[::-1]:
            print("|", item, "|")



if __name__ == "__main__":
    # initialize the object
    stack = Stack()

    # push item to the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)

    # pop items from the stack
    stack.pop()
    stack.pop()

    # traverse through the stack
    stack.traverse()

