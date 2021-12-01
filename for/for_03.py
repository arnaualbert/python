import pprint
import random
import copy

#-------------------------------------------------------------------------------------------------------------------------------------
# Recibe tres nombres por teclado
# guardalos en una lista
# recorre la lista imprimiendolos
# reversed
# pedir tres numeros con input , recorrerlos y sumarlos

# names: list[str] = []

# ej 1,2,3,4

# create empty list
names: list[str] = []

# input names and save in the list names
name1: str = input("Escribe tu nombre: ")
names.append(name1)
name2: str = input("Escribe tu nombre: ")
names.append(name2)
name3: str = input("Escribe tu nombre: ")
names.append(name3)

for name in names:
    print(name)

names_reversed: list[str] = list(reversed(names)) #list es un constructor (construye listas)
print(names_reversed)