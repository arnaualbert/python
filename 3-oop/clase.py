from collections import OrderedDict

# ---------------------------------------------------------------------------------------------------------------------
class Dog:

    species: str = "Canis lupus familiaris "

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
    
    def __str__(self) -> str:
        return f"{self.name} is: a {Dog.species} is {self.age} years old"

# Functions outside oF dog class
# ----------------------------------------------------------------------------------------------------------------------
def show_attributes(something):

    keys = sorted(something.__dict__.keys())
    values = [something.__dict__[key] for key in keys]

    for key, value in zip(keys, values):
        print(f"{key}: {value}")



# Main
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    sarah : Dog = Dog("Sarah",4)
    james: Dog = Dog("James",3)

    print(sarah, james,sep="\n")

    show_attributes(sarah)
    show_attributes(james)
    show_attributes(Dog)

    # podemos acceder a los atributos de classe e instancia desde fuera

    # print(james.name)

    # podemos cambiar atributos de instancia
    sarah.name = "sara connor"

    # se pueden canbiar atributos de clase
    Dog.species = "Cannid lupus lupus"
    # show(Dog)