from pathlib import Path

def get_file(csv_file: str) -> str:
    contents: str = Path("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv").read_text()
    return contents

def get_rows(contents:str) -> list[str]:
    lines: str = contents.split("\n")
    rows: list[str] = []
    rows.append(lines)
    return rows

def get_column(rows: list[str]) -> list[list[str]]:
    table: list[list[str]] = [[]]
    str(rows)
    return table

def get_dosis(table: list[list[str]]) -> list[list[int]]:
    pass

def get_sum(dosis: list[list[int]]) -> tuple[int,int,int]:
    pass

get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv")
print(get_rows(get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv")))
print(get_column(get_rows(get_file("/home/arnaualbert/Desktop/Python/2022-01-20-covid-dades/2022-01-20-covid-dades-simple.csv"))))