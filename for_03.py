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
names: list[str] = []


print("Escribe tu nombre: ")
name1: str = input()
names.append(name1)
print("Escribe tu nombre: ")
name2: str = input()
names.append(name2)
print("Escribe tu nombre: ")
name3: str = input()
names.append(name3)

for name in names:
    print(name)

names_reversed: list[str] = list(reversed(names)) #list es un constructor (construye listas)
print(names_reversed)