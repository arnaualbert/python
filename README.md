#  Apuntes Python

# Indice

# - [Brackets](#Brackets) 

# - [Funcion pura](#Funcion-pura) 

# - [For](#For)

# - [Condicionales if o elif](#Condicionales-if-o-elif) 

# - [While](#While)

# - [Assert](#Assert)

# - [List comprehension](#List-comprehension)

# - [Tools](#Tools)

# - [TIPS](#TIPS)

# Brackets

() brackets 

[] square

{} curly

<> angle

" double quotes

' quote

# Funcion pura

Funcion pura

1 Solo lee parametros de entrada 

2 Solo escribe en sus parametros de salida 

3 Para los mismos parametros de entrada siempre devuelve los mismos parametros de salida

Classe = Tipo

Objeto = Variable

Metodo = Funcion 

sorted es una funcion pura

condicionales y bucles (loops)

1 for = sirve para hacer recorridos de colecciones (listas, str, tuplas...)

2 if

3 while

# For   

sintax :

    names: str = ["Jhon", "Mary", "Lucy"]

    for name in names:

        print(f"hola{name})


name crea una nueva variable

Variables : LOCALES Y GLOBALES

Locales : Las variables que estan dentro de una funcion. solo la funcion tiene acceso a ella

Globales : Las variables que estan fuera de una funcion. estan en el modulo y todo el mundo tiene acceso a ella

# Condicionales if o elif

Condicionales: (expresionbooleana es un true o un false)

    if_expresionbooleana:

        se ejecuta si la expresion booleana es cierta

    else:

        se ejecuta si la expresion booleana es falsa

elif

    if_expresionbooleana:

        se ejecuta si la expresion booleana es cierta
        
    elif:

        se ejecuta si la expresion booleana es cierta pero diferente

Los bool siempre empiezan entre is o are

# While

While sirve para buscar algo y parar en medio

while

    while (condition):
    
        #body...
    
        #body,..
    
        #body...

While ejecuta el body mientras la condicion sea true

1.Mira la condicion

2.Si es true ejecuta el body

3.Despues de ejecutar el body salta a la condicion otra vez

4.Si el condicion es false acaba

5.La actualizacion de finished se tiene que hacer al final

# Assert

assert es un if que si falla tu programa termina

Condicion de assert tiene que ser True  si no mensage de error

No es un funcion (assert) , nunca poner parentesis despues de assert

assert

        assert (num >= 0), "Error: Factorial of a negative number is undefined!"

# List comprehension

Sirve para crear una nueva lista a partit de otra, la original no de modifica

Es como escribir un bucle for pero en una sola linea

Se empieza por el medio

    cube_list = [num **3  for num in [1,2,3]]
                    3        1         2

# Tools :

PyTest

MyPy

PyLint

# TIPS

F10: ejecuta linea

F11: meterse dentro de la funcion

shift+F11: salir de la funcion

F5: debug

F2: renombra

loop and rolling : desenrollar un bucle

dir : lista variables

type : dice el tipo

id :  donde esta en la memoria