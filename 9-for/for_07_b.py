# recorrer una lista de nombres mostrando su indice dentro de la lista

# -----------------------------------------------------------------------------------------------------------
# funcion range hasta 3 parametros, rangedevuelve un iterable asi q necesita un constructor

#  un parametro
print(list(range(5)))  # excluye el ultimo numero de el 0 al 4

# dos parametros
print(list(range(3, 6)))  # excluye el ultimo numero de el 3 al 5

# tres parametros
# el dos es el step quiere decir de cuanto en cuanto cuenta
print(list(range(1, 11, 2)))

# solucion 2 indice escrito manualmente
names: list[str] = ["John", "Mary", "Lucy"]
index_list: list[int] = list(range(len(names)))

for index in index_list:
    print(names[index])
