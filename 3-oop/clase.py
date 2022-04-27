



# ---------------------------------------------------------------------------------------------------------------------
class Dog:

    species: str = "Canis lupus familiaris "

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
    
    def __str__(self) -> str:
        return f"{self.name} is: {self.age} years old"

# Functions outside oF dog class
# ----------------------------------------------------------------------------------------------------------------------
def show(something):

    print(something.__dict__)



# Main
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    sarah : Dog = Dog("sarah",4)
    james: Dog = Dog("James",3)
    print(sarah, james, sep="\n")

    show(sarah)
    show(james)
