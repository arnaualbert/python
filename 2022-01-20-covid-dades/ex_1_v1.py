from pathlib import Path

def get_file(csv_file: str) -> str:
    contents: str = Path("2022-01-20-covid-dades-simple.csv").read_text()
    stripped_contents: str = contents.strip()
    return stripped_contents

def get_rows(contents:str) -> list[str]:
    lines: list[str] = contents.split("\n")
    return lines

def get_columns(rows: list[str]) -> list[list[str]]:
    table: list[list[str]] = []

    for row in rows:
        splitted_row: list[str] = row.split(";")
        table.append(splitted_row)

    return table

def get_dosis(table: list[list[str]]) -> list[list[int]]:
    pass

def get_sum(dosis: list[list[int]]) -> tuple[int,int,int]:
    pass

# get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv")
# print(get_rows(get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv")))
# print(get_column(get_rows(get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv"))))


contents: str             = get_file("2022-01-20-covid-dades-simple.csv")
rows:     list[str]       = get_rows(contents)
table:    list[list[str]] = get_columns(rows)

for row in table:
    print(row)



