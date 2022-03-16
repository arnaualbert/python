
import table
import operator
from pathlib import Path

"""
Exercici 4:

- Fes un programa que llegeixi les dades covid del fitxer adjunt i calculi el següent:
- Ranking d'àrees (NOM) per número de morts (EXITUS).
- Primer mostrar les àrees amb més morts i al final les de menys morts.
- El programa només rep un paràmetre: el nom del fitxer .csv amb les dades covid.
- El programa ha de rebre el nom del fitxer des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

Pasos recomanats:
1. Filtrar per nom d'àrea
2. Sumar els morts d'una àrea
3. Llistar les àrees úniques
4. Per cada àrea calcular la suma total de morts
5. Ordenar àrees pel total de morts
6. Llegir csv per la línea d'ordres
"""

def get_table():

    tabla = table.read_table('2022-03-09-covid-dades-aga.csv')

    return tabla

def get_muertos(tabla):

    muertos = table.get_column(tabla,"EXITUS")

    exitus = []
    for muerto in muertos:
        number = int(muerto)
        exitus.append(number)

    return exitus

def get_area(tabla):

    area = table.get_column(tabla,"NOM")

    return area

def tuple_list(area, exitus):

    list_tuple: list[tuple] = list(zip(area,exitus))

    return list_tuple, area

    
def dict_result(list_tuple, name):
    vardict: dict[str,int] = {}

    for tup in list_tuple:
        vardict[tup[0]] = 0

    for tup in list_tuple:
        vardict[tup[0]] += tup[1]

    return vardict


def get_good_result(vardict: dict[str, int]):
    good_result = sorted(vardict.items(), key = operator.itemgetter(1), reverse = True)

    for name in enumerate(good_result):
        print(name[1][0],vardict[name[1][0]])
    return good_result



tabla = get_table()

exitus = get_muertos(tabla)

area = get_area(tabla)

list_tuple,area = tuple_list(area, exitus)

vardict = dict_result(list_tuple, area)

get_good_result(vardict)




