class Arctos:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age : int = age
        self.greeting = "soy un lobo"
        self.favorite_food = "barbacoa"
        self.species = "canis lupus arctos"
    def __str__(self) -> str:
        return f"hello my name is {self.name} i'm {self.age} yo, my favorite food is {self.favorite_food} and i'm a {self.species}"
    