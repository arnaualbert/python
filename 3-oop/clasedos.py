class Arctos:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
        self.greeting = "soy un lobo"
        self.favorite_food = "barbacoa"
        self.species = "canis lupus arctos"
    def __str__(self) -> str:
        introduction = f"my name is {self.name}, i'm a {self.species} and i'm {self.age}yo"
        closing = f"i love {self.favorite_food} and {self.greeting}"
        
        return f" {introduction}\n{closing}"
    