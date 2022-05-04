""""Python OOPs Exercise 5: What would be the output of the following program?"""


class Staff:
    def __init__(self, role: str, dept: str, salary: int): 
        """_summary_

        Args:
            role (str): the role
            dept (str): the departament
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

    print(isinstance(teacher, Teacher))

    print(isinstance(teacher,Staff))