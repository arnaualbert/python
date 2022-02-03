from pathlib import Path


def get_file(csv_file: str) -> str:
    contents: str = Path("2022-01-20-covid-dades-aga.csv").read_text()
    stripped_contents: str = contents.strip()
    return stripped_contents


def get_rows(contents: str) -> list[str]:
    lines: list[str] = contents.split("\n")
    return lines


def get_columns(rows: list[str]) -> list[list[str]]:

    table = [row.split(";") for row in rows if "BARCELONA" in row]

    return table


def get_dosis_one(table: list[list[str]]) -> list[int]:

    dosi1_list: list[int] = [int(row[20]) for row in table]

    return dosi1_list


def get_dosis_two(table: list[list[str]]) -> list[int]:

    dosi2_list: list[int] = [int(row[21]) for row in table]

    return dosi2_list


def get_sum_one(dosi1_list: list[int]) -> int:

    sum1: int = sum(dosi1_list)

    return sum1


def get_sum_two(dosi2_list: list[int]) -> int:

    sum2: int = sum(dosi2_list)

    return sum2


def get_diff(sum2: int, sum1: int) -> int:

    dif: int = sum1-sum2

    return dif


contents: str = get_file("2022-01-20-covid-dades-aga.csv")
rows:     list[str] = get_rows(contents)
table:    list[list[str]] = get_columns(rows)
dosis:    list[int] = get_dosis_one(table)
dosis2:   list[int] = get_dosis_two(table)
sum_o:    int = get_sum_one(dosis)
sum_t:    int = get_sum_two(dosis2)
diff:     int = get_diff(sum_t, sum_o)

print(f"El total de vacunados de la primera dosis es : {sum_o}")
print(f"El total de vacunados de la segunda dosis es : {sum_t}")
print(f"La diferencia es : {diff}")
