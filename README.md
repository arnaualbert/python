# python

() brackets 

[] square

{} curly

<> angle

" double quotes

' quote

Funcion pura

1 solo lee parametros de entrada 

2 solo escribe en sus parametros de salida 

3 para los mismos parametros de entrada siempre devuelve los mismos parametros de salida

classe = tipo

objeto = variable

metodo = funcion 

sorted es una funcion pura

condicionales y bucles (lops)

1 for = sirve para hacer recorridos de colecciones (listas, str, tuplas...)

2 if

3 while

1 for   

sintax :

    names: str = ["Jhon", "Mary", "Lucy"]

    for name in names:

        print(f"hola{name})


name crea una nueva variable

variables : LOCALES Y GLOBALES

locales : Las variables que estan dentro de una funcion. solo la funcion tiene acceso a ella

globales : Las variables que estan fuera de una funcion. estan en el modulo y todo el mundo tiene acceso a ella

F10: ejecuta linea

F11: meterse dentro de la funcion

shift+F11: salir de la funcion

F5: debug

F2: renombra

loop and rolling : desenrollar un bucle

dir : lista variables

type : dice el tipo

id :  donde esta en la memoria

condicionals: (expresionbooleana es un true o un false)

    if_expresionbooleana:

        se ejecuta si la expresion booleana es cierta

    else:

        se ejecuta si la expresion booleana es falsa

elif

    if_expresionbooleana:

        se ejecuta si la expresion booleana es cierta
        
    elif:

        se ejecuta si la expresion booleana es cierta pero diferente

los bool siempre empiezan entre is o are

while sirve para buscar algo y parar en medio

while

    while (condition):
    
        #body...
    
        #body,..
    
        #body...

while ejecuta el body mientras la condicion sea true

1.mira la condicion

2.si es true ejecuta el body

3.despues de ejecutar el body salta a la condicion otra vez

4.si el condicion es false acaba

5.la actualizacion de finished se tiene que hacer al final

assert es un if que si falla tu programa termina

condicion de assert tiene que ser True  si no mensage de error

no es un funcion (assert) , nunca poner parentesis despues de assert

assert

        assert (num >= 0), "Error: Factorial of a negative number is undefined!"

Tools :

PyTest

MyPy

PyLint

