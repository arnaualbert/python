import pprint
import random
import copy

#-------------------------------------------------------------------------------------------------------------------------------------

# recorrer una lista de nombres mostrando su indice de la lista

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
    print(name.index(name))