"""Python OOPs Exercise 4: Write a Program, to create class and using the class instance print all the writable attributes of that object."""

class Staff:
    def __init__(self, role: str, dept: str, salary: int): 
        """_summary_

        Args:
            role (str): the role
            dept (str): the deopartament
            salary (int): the salary
        """
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        """show the details of the class
        """
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department", self.dept)

#inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name: str, age: int):
        """_summary_

        Args:
            name (str): the name
            age (int): the age
        """
        self.name = name
        self.age = age
        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)


if __name__ == "__main__":
    teacher = Teacher("Raj", 45)

    #display all the namespaces
    print(teacher.__dict__)