# classes
class CanisLupus:
    def __init__(self,name: str,age: int) -> None:
        self.name = name
        self.age = age    
    
    def __str__(self) -> str:
        introduction = f"me llamo es {self.name} y tengo {self.age} años"

        return f" {introduction}"
    
    

# modulo
if __name__ == "__main__":
    pass