# recorrer una lista de nombres mostrando su indice dentro de la lista

#-----------------------------------------------------------------------------------------------------------

# solucion 1 indice escrito manualmente
names: list[str] = ["John", "Mary", "Lucy"]
index_list: list[int] = [0, 1, 2]

for index in index_list:
    print(names[index])