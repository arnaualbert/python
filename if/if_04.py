import pprint
import random
import copy

age: int = 100 # años

is_baby: bool = (0 <= age <= 1)

is_child:bool = (2 <= age <= 6)

is_adult:bool = (7 <= age <= 90)

is_elder:bool = (90 <= age)

if is_baby: # si se cumplen las dos cosas
    print("regalar pañales")
elif is_child:
    print("regalar pelota")
elif is_adult:
    print("regalar ropa")
elif is_elder:
    print("regalar pañales")