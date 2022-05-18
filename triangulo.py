# Arnau Albert Sanchez

def triangulo(l1,l2,l3):

    lista_lados = [l1,l2,l3]

    lado_grande = max(lista_lados)

    total = l1 + l2 + l3

    es_un_triangulo = lado_grande < total

    es_equilatero = (l1 == l2) and (l2 == l3)

    es_isosceles = ((l1 == l2) or (l2 == l3) or (l3 == l1))

    tipo_triangulo: str = ""
    if not es_un_triangulo:
        tipo_triangulo = "no es un triangulo"
    elif es_equilatero:
        tipo_triangulo = "trianfulo equilatero"
    elif es_isosceles:
        tipo_triangulo = "triangulo isosceles"
    else: 
        tipo_triangulo = "triangulo escaleno"

    return tipo_triangulo

if __name__ == "__main__":

    print(triangulo(10,10,10)) # trianfulo equilatero

    print(triangulo(1,10,8)) # triangulo escaleno

    print(triangulo(3,2,3)) # triangulo isosceles
    
    print(triangulo(-30,2,1)) # no es un triangulo

    print(triangulo(10,10)) # error falta un parametro

    print(triangulo(10,10,A)) # los parametros tienen que ser enteros o floats

    print(triangulo(10,10,20,20)) # sobra un numero