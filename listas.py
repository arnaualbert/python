import pprint
import random
import copy
# Lists

# list literals
l1: list = [] # lista vacia
l2: list[str] = ["John", "Mel", "Lucy"] # Los subtipos van entre []

# lenght of a list
l2_len: int = len(l2)

# element acces

print(l2[0]) #John
print(l2[2])  #Lucy
print(l2[-1])   #Lucy
print(l2[len(l2)-1]) #Lucy

l2[2][0] # "Lucy"[0]

# sublistas

l3: list[str] = ["a", "b", "c", "d", "e", "f"]
print(l3[0:4]) # a,b,c,d
print(l3[4:6]) # e,f
print(l3[4:]) # e,f

# list operation
print(["John", "Mary", "Lucy"]+["Peter", "Isaac"])
print([1,2,3] * 3) #repite elementos

# multiple types in a list not recomended
l4:list[object] = print([1,"John", True,0.9])
l5:list[list[int]] = [[1,2],[3,4]]

first_row = l5[0]
second_row = l5[1]
print(f"{first_row}\n{second_row}")

# search elements

l6:list[str] = ["a", "b", "c","d","e","f"]
print(l6.index("d")) #da la posicion

# count

l6:list[str] = ["a", "b", "b", "c","c","c","d","e","f"]
print(l6.count("c")) # cuenta elementos

# sorted 
# sorted te devuelve una nueva lista 
l6: list[int] = [4,2,1,3,0]
l6_sorted: list[int] = sorted(l6)
print(l6_sorted)

# reversed
# devuelve una lista girada
l6: list[int] = [1,2,3,4]
l6_reversed: list[int] = list(reversed(l6))
print(l6_reversed)

#----------------------------------------------------------------------------------------------------------------------------------------

# en python todoas las funciones deveulven algo 
# si no return keyboard they return NONE

#Funcion pura
#1 solo lee parametros de entrada 
#2 solo escribe en sus parametros de salida 
#3 para los mismos parametros de entrada siempre devuelve los mismos parametros de salida

# ejemplo 1
a = 1
def do_something_v1():
    print(a)

do_something_v1()

def do_something_v2():
    b = input()
    print(b)

do_something_v2

# ej 2
l6: list[int] = [1, 2, 3]
l6.append(4) # return none

#ej3
def do_something_v3():
    return random.randint(1,10)
do_something_v3()

#-------------------------------------------------------------------------------------------------------------------------------------
# assignment List are mutable

l3[0] = "z" #cambia la letra en posicion 0 por z 
l3[0] = "a"
print(l3)

# slice assignment

l3[3:] = [1,2,3] # d,e,f por 1,2,3
l3[3:] = ["d"] # new assigment can be different lenghts
l3[3:] = [] # borras lo que hay apartir de el num
l3 = [] # borra todo
l3[:] = [] #borra todo
print(l3)

# list methods
l3_methods: list[str] = dir(l3)
pprint.pp(l3_methods)

# append

l3: list[int] = [0, 1, 2 , 3, 4, 5]
l3.append(6)
print(l3)

# extend 

l6: list[int] = [1,2,3]
l7: list[int] = [4,5,6]
l8: list[int] = l6 + l7 # pure
print(l8)


l6.extend(l7) # mejor no hacer (extiene la lista 6 con la lista 7)
print(l6) # mejor la suma line 192 q la linea 106

# insert (no sobreescribe)

l6.insert(0,10) #inserta el num 10 en la psoicion 0
l6.insert(len(l6),10) # inserta 10 al final
print(l6)

# remove

l6.remove("b") #remove the element
print(l6)


#pop
#removes by index
l6.pop(1)
print(l6)

# clear
#lo borra todo pero deja la funcion
l6.clear()



# "del" keyword

# del no es una funcione es una palabra clave
# no hay q poner parentesis depsues de del
# del lo borra todo
l6:list[str] = ["a","b","c","d"]
del l6[3]
del l6[:] # borra todos los elementos de la lista
print(l6)
del l6 # borra la lista




#--------------------------------------------------------------------------------------------------------------------------------------------

l6: list[int] = [1,2,3]
l7: list[int] = copy.copy(l6)
print(l6)
print(l7)




#------------------------------------------------------------------------------------------------------------------------------------------
# prints
print(l2_len)

print(l1)
print(len(l2))