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

        canis_lupus_phrase = super().__str__() # llama al __str__ de canis lupus 
        lola_phrase = "a cup of cafe con leche in Plaza Mayor"
        return canis_lupus_phrase + "\n" + lola_phrase


class SignatusSiestus(Signatus):

    def __init__(self,name: str, age: int,nana):
        self.nana = nana
        self.ronquido = "z"

        # self.greeting = "soy un lobo iberico"
        # self.favorite_food = "paella"
        # self.species = "canis lupus signatus"

    def __str__(self) -> str:

        siesta = self.ronquido
        return siesta
        
    def from_nana(self):
        if self.nana == "nana":
            self.ronquido = "zzzzz"
        else:
            self.ronquido = "hahahah"
        

    
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
    antonio = SignatusSiestus("antonio",4,"nana")


    print(cani)
    print(anya)
    print(miguel)
    print(rafa)
    print(antonio)

    print(f"antonio es de tipo : {type(antonio)}") # para saber el tipo
    print(f"antonio es un signatus? {isinstance(antonio, Signatus)}") # para preguntar si es una instancia
    print(f"antonio es un CanisLupus? {isinstance(antonio, CanisLupus)}") # para preguntar si es una instancia
    print(f"antonio es un Arctos? {isinstance(antonio, Arctos)}") # para preguntar si es una instancia

    show_attributes(antonio)
    # show_attributes(anya)
