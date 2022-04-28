# classes
class CanisLupus:
    def __init__(self,name: str,age: int) -> None:
        self.name = name
        self.age = age    
    
    def __str__(self) -> str:
        
        introduction = f"me llamo es {self.name}, soy un {self.species} y tengo {self.age} años"
        closing = f"mi comida favorita es {self.favorite_food} y {self.greeting}"

        return f" {introduction}\n{closing}"
    


# modulo
if __name__ == "__main__":
    cani = CanisLupus("CANI",4)