import random

def escoger_opcion(opcion):

    eleccion: str = random.choice(opcion)

    return eleccion

opcion1 = input("Dime la opcion uno: ")
opcion2 = input("Dime la opcion dos: ") 

opcion: list[str] = [opcion1,opcion2]
print(escoger_opcion(opcion))