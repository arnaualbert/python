import pprint

s1: str = "esto es un string. UN string es un texto"
s2: str = 'esto es un string. UN string es un texto'

s3: str = "it's a trap!"
s4: str = 'she said "i love it"'
s5: str = """"she said "i'm bussy!"""""

s6: str = "las comillas simples y las dobles son identicas"

s7: str = "a" #string de una sola letra no hay char en python

s8: str = """comillas triples"""

#---------------------------------------------------------------------------------------------------

s1: str = "hello"
s1[1] = "o"
s1
pprint.pp(dir(s1))

s2 = s1.upper()

#substring
print(s1)
print(s1[:])
print(s1[0:])
print(s1[0:5])
print(s1[0:len(s1)])

len(s1) #devuelve la longitud

#Funciones basicas : type(), id(), dir()
#cuando se importa una libreria no se tiene que poner from --- import * se tiene que hacer import ---- as el nombre que tu quieras

#----------------------------------------------------------------------------------------------------------------------------

# string normal
normal_string: str = "hello\nworld"
print(normal_string)

# un raw string te pone lo que pones literalmente
raw_string: str = r"hello\nworld"
raw_string2: str = "hello\\nworld"
print(raw_string)
print(raw_string2)

# forma mas facil de mezclar strings con variables
name: str = "Arnau"
format_string: str = f"hello {name}"
print(format_string)

#------------------------------------------------------------------------------------------------------------------------------------------

#operaciones con strings

# suma de strings
greeting: str = "Hello"
name: str = "World"
space: str = " "
bang: str = "!"
concat: str = greeting + " " + name + bang
concat2: str = greeting + space + name + bang

print(f"{greeting} {name}")
print(greeting + name)
print(greeting, name)
print(concat)

# multplicacion string (repeticion)
print("hello " * 3)