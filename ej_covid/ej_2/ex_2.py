from pathlib import Path


def get_file(csv_file: str) -> str:
    contents: str = Path("2022-01-20-covid-dades-aga.csv").read_text()
    stripped_contents: str = contents.strip()
    return stripped_contents


def get_rows(contents: str) -> list[str]:
    lines: list[str] = contents.split("\n")
    return lines


def get_columns(rows: list[str]) -> list[list[str]]:
    table: list[list[str]] = []

    for row in rows:
        if "BARCELONA" in row:
            splitted_row: list[str] = row.split(";")
            table.append(splitted_row)
    return table 


def get_dosis_one(table: list[list[str]]) -> list[int]:

    dosi1_list: list[int] = []

    for row in table:
        dosi1_list.append(int(row[20]))

    return dosi1_list


def get_dosis_two(table: list[list[str]]) -> list[int]:
    # dosis2: list[list[int]] = []
    # index = 0
    # b: list[int]= []
    # for i in table:
    #     b.append(table[index][6])
    #     index = index + 1
    # del b[0]
    # dosis2.append(b)
    # print(dosis2)
    dosi2_list: list[int] = []

    for row in table:
        dosi2_list.append(int(row[21]))

    return dosi2_list


def get_sum_one(dosi1_list: list[int]) -> int:  # tuple[int,int,int]:
    # for i in range(len(dosis)):
    #     dosis[i] = list[int](dosis[i])
    # sum_one = sum(dosis)
    # int_list = [int(i) for i in dosis]
    # sum_one = sum(int_list)
    # return sum_one
    sum1: int = sum(dosi1_list)

    return sum1


def get_sum_two(dosi2_list: list[int]) -> int:  # tuple[int,int,int]:
    # for i in range(len(dosis)):
    #     dosis[i] = list[int](dosis[i])
    # sum_one = sum(dosis)
    # int_list = [int(i) for i in dosis]
    # sum_one = sum(int_list)
    # return sum_one
    sum2: int = sum(dosi2_list)

    return sum2

def get_diff(sum2: int,sum1: int) -> int:

    dif: int = sum1-sum2

    return dif
# get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv")
# print(get_rows(get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv")))
# print(get_column(get_rows(get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv"))))


contents: str = get_file("2022-01-20-covid-dades-aga.csv")
rows:     list[str] = get_rows(contents)
table:    list[list[str]] = get_columns(rows)
dosis:    list[int] = get_dosis_one(table)
dosis2:   list[int] = get_dosis_two(table)
sum_o:    int = get_sum_one(dosis)
sum_t:    int = get_sum_two(dosis2)
diff:     int= get_diff(sum_t,sum_o)

print(f"El total de vacunados de la primera dosis es : {sum_o}")
print(f"El total de vacunados de la segunda dosis es : {sum_t}")
print(f"La diferencia es : {diff}")
# for row in table:
#     print(row)
