class Arctos:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
        self.greeting = "soy un lobo artico"
        self.favorite_food = "barbacoa"
        self.species = "canis lupus arctos"
    def __str__(self) -> str:
        introduction = f"my name is {self.name}, i'm a {self.species} and i'm {self.age} years old"
        closing = f"i love {self.favorite_food} and {self.greeting}"

        return f" {introduction}\n{closing}"

class Baileyi:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
        self.greeting = "soy un lobo mexicano"
        self.favorite_food = "burritos"
        self.species = "canis lupus baileyi"
    def __str__(self) -> str:
        introduction = f"my nombre es {self.name}, soy un {self.species} y tengo {self.age} años"
        closing = f"me encanta {self.favorite_food} y {self.greeting}"

        return f" {introduction}\n{closing}"

class Signatus:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
        self.greeting = "soy un lobo iberico"
        self.favorite_food = "paella"
        self.species = "canis lupus signatus"
    def __str__(self) -> str:
        introduction = f"my llamo es {self.name}, soy un {self.species} y tengo {self.age} años"
        closing = f"mi comida favorita es {self.favorite_food} y {self.greeting}"

        return f" {introduction}\n{closing}"

if __name__ == "__main__":
    anya = Arctos("anya",4)
    miguel = Baileyi("miguel",4)
    rafa = Signatus("rafa",4)