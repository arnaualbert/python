# classes
# ----------------------------------------------------------------------------------------------------------------------
class CanisLupus:
    def __init__(self,name: str,age: int) -> None:
        self.name = name
        self.age = age  
        self.greeting = "i'm a wolf"
        self.favorite_food = "meat"
        self.species = "canis lupus"  
    
    def __str__(self) -> str:
        introduction = f"my name is {self.name}, i'm a {self.species} and i'm {self.age} years old"
        closing = f"i love {self.favorite_food} and {self.greeting}"

        return f" {introduction}\n{closing}"

class Arctos(CanisLupus):

    def __init__(self, name: str, age: int):

        super().__init__(name, age)

        self.greeting = "i'm a cool wolf"
        self.favorite_food = "polar bear barbacue"
        self.species = "canis lupus arctos"

class Baileyi(CanisLupus):

    def __init__(self, name: str, age: int):

        super().__init__(name, age)

        self.greeting = "soy un lobo mexicano"
        self.favorite_food = "burritos"
        self.species = "canis lupus baileyi"
                                

class Signatus(CanisLupus):

    def __init__(self, name: str, age: int):

        super().__init__(name, age)

        self.greeting = "soy un lobo iberico"
        self.favorite_food = "paella"
        self.species = "canis lupus signatus"

    def __str__(self) -> str:

        canis_lupus_phrase = super().__str__()
        lola_phrase = "a cup of cafe con leche in Plaza Mayor"
        return canis_lupus_phrase + "\n" + lola_phrase

        
    
# Functions outside of dog class
# ----------------------------------------------------------------------------------------------------------------------
def show_attributes(something):

    keys = sorted(something.__dict__.keys())
    values = [something.__dict__[key] for key in keys]

    for key, value in zip(keys, values):
        print(f"{key}: {value}")


# modulo
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    cani = CanisLupus("CANI",4)
    anya = Arctos("anay", 4)
    miguel = Baileyi("miguel",4)
    rafa = Signatus("rafa",4)


    print(cani)
    print(anya)
    print(miguel)
    print(rafa)

    # show_attributes(cani)
    # show_attributes(anya)