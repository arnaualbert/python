import pprint
import random
import copy

edad: int = 91 # años

if (0 <= edad <= 1): # si se cumplen las dos cosas
    print("regalar pañales")
    # edad > 1 
elif (1 <= edad <= 6):
    print("regalar pelota")
    # edad > 6 
elif (6 <= edad <= 90):
    print("regalar ropa")
    # edad > 90
elif(90 < edad):
    print("regalar pañales")