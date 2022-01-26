from pathlib import Path

def get_file(csv_file: str) -> str:
    contents: str = Path("2022-01-20-covid-dades-simple.csv").read_text()
    return contents

def get_rows(contents:str) -> list[str]:
    # lines: str = contents.split("\n")
    pass

def get_column(rows: list[str]) -> list[list[str]]:
    pass

def get_dosis(table: list[list[str]]) -> list[int]:
    pass

def get_sum(dosis: int) -> int:
    pass
