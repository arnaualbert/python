"""Python OOPs Exercise 3: Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff"""

class Staff():
    def __init__(self, role, dept, salary): 
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department:", self.dept)

class Teacher(Staff):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Teacher","Science",25000)


if __name__ == "__main__":
    teacher = Teacher("Raj", 28)
    #access the Staff Method
    teacher.show_details()