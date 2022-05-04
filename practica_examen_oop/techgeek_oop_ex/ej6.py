"""Python OOPs Exercise 6: Create a class Teacher with name, age, and salary attributes, where salary must be a private attribute that cannot be accessed outside the class. """


class Teacher():
    def __init__(self, name: str, age: int, salary: int):
        """_summary_

        Args:
            name (str): the name
            age (int): the age
            salary (int): the salary
        """
        
        self.name = name
        self.age = age

        # private variable
        self.__salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

        #access private attribute inside the class
        print("Salary: ", self.__salary)

if __name__ == "__main__":
    teacher = Teacher("Raj", 45, 25000)

    teacher.show_details()

    # print(teacher.name)   #Raj

    #access private member outside the class will throw error
    # print(teacher.__salary)   #error