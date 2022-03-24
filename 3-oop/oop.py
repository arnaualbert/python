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