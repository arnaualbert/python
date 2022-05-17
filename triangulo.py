def triangulo():

    l1 = int(input("dime el primer lado: "))

    l2 = int(input("dime el primer lado: "))

    l3 = int(input("dime el primer lado: "))

    lista_lados = [l1,l2,l3]

    if l1 or l2 or l3 == int:
        print(f"estos son tus lados {lista_lados}")
    else:
        raise Exception("Pon numeros")


    if l1 and l2 and l3 > 0:
        print("por ahora vas bien")
    else:
        raise Exception("Numeros positivos")

    lado_grande = max(lista_lados)

    total = l1 + l2 + l3

    if lado_grande > l2 + l3 or lado_grande > l1 + l2 or lado_grande > l3 + l1:
        raise Exception("el lado grande debe ser menor que la suma de los otros lados")
    

    if lado_grande < l2 - l3 or lado_grande < l1 - l2 or lado_grande < l3 - l1:
        raise Exception("el lado grande debe ser mayor que la resta de los otros lados")

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

    print(triangulo())