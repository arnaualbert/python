



# ---------------------------------------------------------------------------------------------------------------------
class Dog:

    species: str = "Especie"
    
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
    
    def __str__(self) -> str:
        return f"{self.name} is: {self.age} years old"


# Main
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "main":

    sarah : Dog = Dog("sarah",4)
    james: Dog = Dog("James",3)
    print(sarah, james, sep="\n")

