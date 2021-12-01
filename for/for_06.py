# crear una lista con nombres y otra vacia
# copiar todos los nombres en la lista vacia.
# --------------------------------------------------------------------------------------------------------------

names: list[str] = ["John", "Mary", "Lucy"]
new_list: list[str] = []

for name in names:
    new_list.append(name)

print(new_list)
