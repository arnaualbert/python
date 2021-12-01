import pprint
import random
import copy

edad: int = 91  # años

if (0 <= edad <= 1):  # si se cumplen las dos cosas
    print("regalar pañales")
else:
    # edad > 1
    if (1 <= edad <= 6):
        print("regalar pelota")
    else:
        # edad > 6
        if (6 <= edad <= 90):
            print("regalar ropa")
        else:

            if(90 < edad):
                print("regalar pañales")
