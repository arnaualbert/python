#  Apuntes Python

# Indice

## - [Brackets](#Brackets) 

## - [Funcion pura](#Funcion-pura) 

## - [For](#For)

## - [Condicionales if o elif](#Condicionales-if-o-elif) 

## - [While](#While)

## - [Assert](#Assert)

## - [List comprehension](#List-comprehension)

## - [Dictionary](#Dictionary)

## - [Lambda](#Lambda)

## - [Tools](#Tools)

## - [Servidor python](#Servidor-python)

## - [Recursion](#Recursion)

## - [Ejecutable python](#Ejecutable-python)

## - [OOP](#OOP)

## - [Exception](#Exception)

## - [Flask](#Flask)

## - [TIPS](#TIPS)

# Brackets

() brackets 

[] square

{} curly

<> angle

" double quotes

' quote

### - [Ir al índice](#Indice).

# Funcion pura

Funcion pura

1 Solo lee parametros de entrada 

2 Solo escribe en sus parametros de salida 

3 Para los mismos parametros de entrada siempre devuelve los mismos parametros de salida

Classe = Tipo (int,bool,float)

Objeto = Variable (entrada en la tabla de simbolos)

Metodo = Funcion (funcion asociada a un objeto)

sorted es una funcion pura

condicionales y bucles (loops)

1 for = sirve para hacer recorridos de colecciones (listas, str, tuplas...)

2 if

3 while

### - [Ir al índice](#Indice).

# For   

sintax :

```python
    names: str = ["Jhon", "Mary", "Lucy"]

    for name in names:

        print(f"hola{name})
```


name crea una nueva variable

Variables : LOCALES Y GLOBALES

Locales : Las variables que estan dentro de una funcion. solo la funcion tiene acceso a ella

Globales : Las variables que estan fuera de una funcion. estan en el modulo y todo el mundo tiene acceso a ella

#### - [ej_for](for)

### - [Ir al índice](#Indice).

# Condicionales if o elif

Condicionales: (expresionbooleana es un true o un false)

```python
    if expresionbooleana:

        se ejecuta si la expresion booleana es cierta

    else:

        se ejecuta si la expresion booleana es falsa

elif

    if expresionbooleana:

        se ejecuta si la expresion booleana es cierta
        
    elif:

        se ejecuta si la expresion booleana es cierta pero diferente
```

Los bool siempre empiezan entre is o are

#### - [ej_if](if)

### - [Ir al índice](#Indice).

# While

While sirve para buscar algo y parar en medio

while

```python
count: int = 0
finished: bool = (count > 3)


while not finished:

    # body
    print(count)

    # update finishing condition
    count = count + 1
    finished = (count > 3)
```

While ejecuta el body mientras la condicion sea true

1.Mira la condicion

2.Si es true ejecuta el body

3.Despues de ejecutar el body salta a la condicion otra vez

4.Si el condicion es false acaba

5.La actualizacion de finished se tiene que hacer al final

#### - [ej_while](while)

### - [Ir al índice](#Indice).

# Assert

assert es un if que si falla tu programa termina

Condicion de assert tiene que ser True  si no mensage de error

No es un funcion (assert) , nunca poner parentesis despues de assert

assert

```python
assert (num >= 0), "Error: Factorial of a negative number is undefined!"
```

### - [Ir al índice](#Indice).

# List comprehension

Sirve para crear una nueva lista a partit de otra, la original no de modifica

Es como escribir un bucle for pero en una sola linea

Funcion pura

Se empieza por el medio

```python
    cube_list = [num **3  for num in [1,2,3]]
                    3        1         2

    newlist = [expression for item in iterable if condition == True]
```

### - [Ir al índice](#Indice).

# Dictionary

Para hacer un diccionario va bien poner los tipos

Es una estructura de datos que nos permite almacenar parejas de datos : clave y valor

La ventaja de los diccionarios de que nos permite buscar los valores por clave rapidamente

Para buscar un  diccionario[clave]

Para saber las claves diccionario.key()

Para saver los valores diccionario.value()

Para insertar un valor en el diccionario es diccionario[clave] - valor

Para juntar diccionarios es dict(zip(dic1,dic2))

Copiar diccionario en diccionario dict2.update(dic) pone los datos de dic en dic2


```python
    agenda: dict[str,int] = {}#diccionario vacio

    agenda["Gabriel"] - 123

    agenda = {"Gabriel": 123, "Alex":456, "Pau":789}#diccionario con claves y sus valores
                clave    valor
                key      value
```

### - [Ir al índice](#Indice).

# Lambda

es una funcion anonima (sin nombre)

sirve para cuando se quieren hacer funciones pero se ponen como un parametro

la funcion se escribe a la derecha : key=lambda item: item[1]

se pensaron para hacer funciones cortyas y sencillas solo permiten una expresion en el cuerpo de la lambda

la lambda devuelve el resultado de la expresion

se suelen usar como parametros en otras funciones

```python
    min(item_list, key=lambda item: item[1])

    def sumar(a,b):
        return a +b

    #igual que:

    sumar2 = lambda a,b: a + b
```

### - [Ir al índice](#Indice).

# Tools

PyTest

MyPy

PyLint

### - [Ir al índice](#Indice).

# Servidor python

SSG STATIC SITE GENERATOR

cliente                           servidor(vendedor) 

navegador(firefox, chrome)      ordenador con programas echos a medida

                                en linux /var/www/html hay archivos html

python -m http.server

127.0.0.1:8000 (direccion propia)

Principales metodos request:

GET

POST (tambien se usa para conseguir datos)

PUT (subir datos al servidor)

DELETE (borrar datos servidor)

UPDATE (actualizar fichero servidor)

### - [Ir al índice](#Indice).

# Recursion

la recursion es como bucles con funciones

Simula bucles usando solo funciones

La recursividad te permite hacer mas cosas que un bucle (mas potente, mas general)

### - [Ir al índice](#Indice).

# Ejecutable python

se pone "#! /usr/bin/env python3" al principio de el archivo

tambien se le tienen que poner permisos al archivo de ejecucion:

chmod u+x nombre_archivo.py #solo para mi

chmod a+x nombre_archivo.py #para todos

se pone el ejecutable en el PATH:

echo $PATH 

echo $PATH | sed 's/:/\n/g'

PATH=~/bin:$PATH

nano ~/.profile

cp hola.py ~/bin/hola

### - [Ir al índice](#Indice).

# OOP

Progamacion oientada a objetos

OOP es el paradigma de programacion mas extendido hoy en dia

Paradigmas de programacion : un paradigma es un conjunto de ideas

El paradigma mas basico es el procedural "procedimientos" "funciones"

El mas popular es el funcional

Tambien existe la programacion logica , ...

Object = DATA + FUNCTIONS

Python OOP (Java,C++,C#)

Se crean objetos cuando se tiene una idea que necesita datos y funciones y sea muy estable

Los objetos tiene instance atribbute, son los que se ponen en self

tiene metodos de instancia (se sabe porque recibe el parametro self)

```python
# Clases empiezan en mayusculas
class BadExample():
    pass

# Las clases tienen un constructor
class Dog():
    def __init__(self) -> None:
       #^^^^^^^^: esto es un constructor
        pass
```

la herencia es un metodo para no repetir codigo

```python
class CanisLupus:
    def __init__(self,name: str,age: int) -> None:
        self.name = name
        self.age = age  
        self.greeting = "i'm a wolf"
        self.favorite_food = "meat"
        self.species = "canis lupus"  
    
    def __str__(self) -> str:
        introduction = f"my name is {self.name}, i'm a {self.species} and i'm {self.age} years old"
        closing = f"i love {self.favorite_food} and {self.greeting}"

        return f" {introduction}\n{closing}"

class Arctos(CanisLupus):

    def __init__(self, name: str, age: int):

        super().__init__(name, age)

        self.greeting = "i'm a cool wolf"
        self.favorite_food = "polar bear barbacue"
        self.species = "canis lupus arctos"
```

@classmethod es un decorador para tener dos constructores

```python
class Table:

    # Constructor
    # -------------------------------------------------------------------------
    def __init__(self, data: list[list[str]]):

        self.data: list[list[str]] = data


    # Alternative Constructor
    # -------------------------------------------------------------------------
    @classmethod # decorador
    def from_csv(cls, csv_file_path: str):

        raw_text:       str             = Path(csv_file_path).read_text()
        stripped_text:  str             = raw_text.strip()
        rows:           list[str]       = stripped_text.split("\n")
        data:           list[list[str]] = [row.split(";") for row in rows]
        table:          Table           = cls(data)

        return table


    # Print
    # -------------------------------------------------------------------------
    def __str__(self) -> str:

        pretty_rows:  list[str] = [', '.join(row) for row in self.data]
        pretty_table: str       =  '\n'.join(pretty_rows)

        return pretty_table

```

### - [Ir al índice](#Indice).



# Exception

Una exception es un objeto que se usa caundo hay un error en mi programa

Una exception contiene lo que tu quieras, como minimo un mensaje de error que se imprime cuando imprimimos la exception

despues de el raise no se ejecuta !! 

si ocurre un error se puede tratar ? 

No : mi programa finalizara

Si : escoger donde tratarlo y poner alli los bloques

Como se crea una exception

```python

Exception("ha habido un error !")

MemoryError("No tienes espacio") # error no tienes memoria

ex : Exception = Exception("hay un error !")

#ejemplo

age : int = 1

if age >= 0:

    print("estas vivo")

else :
    
    raise Exception("edad negativa")

# despues de la excepcion lo de abajo no se ejecuta   

def do_login(...)
    ...              # no se ejecuta porque saltamo a algun sitio
    ...
    ..



try :
    .... # lo que puede fallar
except:
    .... # tratamiento error
    
```

### - [Ir al índice](#Indice).

# Flask

```python

#1 inicializacion
from flask import Flask

app: Flask = Flask(__name__)

#3 rutas

@app.route("/")
def index():
    ...
    ...
    ...

#2 run
if __name__ == "__main__":
    app.run(debug=True)

```

Web dinamica vs estaticas

dinamica: no exixte fichero html a disco

cuando se recive una request se llama a una funcion que genera el codigo html y se devuelve directamente cada vez

este html autogenerado puede cambiar en cada peticion

estatica : existe el archivo html a disco (ssg)

Peticiones GET : Parametros
```python
  http://                          www.myapp.com                /welcome

 protocolo                           dominio                ruta dentro de web         

                                        |
                                        | DNS
                                        |


                                IPv4: 20.34.120.56
```
      

### - [Ir al índice](#Indice).

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

sorted. ordena :  sorted(item_list, key=get_value)

para clonar repositorio es : git clone direccion

Para instalar librerias es : conda install -n py39 -c anaconda "nombre libreria"

rglob lo mira todo subdirectorios incluidos 

siempre que haya un glob/generador/iterador delate un list

libreria : pathlib >>>>>> os
```python
filepath_list: list[Path] = [path for path in path_list if path.is_file()]
                                 3          1                     2
                        1 para cada ruta en la lista de rutas 2 si es un archivo 3 lo mete en la lista                    
```

sys.argv para ejecutar desde terminal

ejecutar desde terminal : python e3.py 'my data' '*.md'

si en un for no vas ha usar una variable se pone barra baja _

hay una libreria menos compleja para sys.argv que se llama argparse

### - [Ir al índice](#Indice).