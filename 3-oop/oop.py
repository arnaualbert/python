class Antena(): 
    color = "gris" 
    longitud = "10m" 

class Pelo(): 
    color = "rubio" 
    textura = "normal" 

class Ojo(): 
    forma = "redondo" 
    color = "azul" 
    tamanio = "pequeño"

class Objeto(): 
    color = "verde" 
    tamanio = "grande" 
    aspecto = "feo" 
    antenas = Antena() 
    ojos = Ojo() 
    pelos = Pelo() 

    def flotar(self): 
        print(12)

et = Objeto() 
at = Antena()
it = Ojo()
ut = Pelo()
print(et.color)
print(et.tamanio)
print(et.aspecto)
et.color = "rosa" 
print(et.color)
print(at.color)
print(at.longitud)
at.longitud = "15m"
print(at.longitud)


'''
Object oriented programing
'''
from pathlib import Path
# Clases empiezan en mayusculas

class BadExample():
    pass

# Las clases tienen un constructor
#on definition we write __init__ ()
#on callinf we called Dog
#methods :
#all methods have a special parameter: self
#when calling the method we don't write it
#attributes:
#attributes are variables stores inside the objects
#they are created by the constructor 
#to access them write self.<attribute>
#-----------------------------------------------------
class Dog():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello i'm {self.name}")
#----------------------------------------------------

# firulais: Dog = Dog("firulais",3)
# dama: Dog = Dog("dama",5)
# firulais.greet()
# dama.greet()

#----------------------------------------------------