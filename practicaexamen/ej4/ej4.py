



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

def make_dict(table: list[list[str]]):

    for dosis in table:
