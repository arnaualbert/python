"""Python OOPs Exercise 1: Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object."""

class Students():

    def __init__(self,name: str,age: int,grade: str) -> None:
        """_summary_

        Args:
            name (str): the name of the student
            age (int): the age of the student
            grade (str): the grade of the student
        """
        
        self.name = name
        self.age = age
        self.grade = grade

if __name__ == "__main__":
    raj = Students('Raj', 16, '11th')