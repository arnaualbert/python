from pathlib import Path

def get_file(csv_file: str) -> str:
    corona_file: str = Path("2022-01-20-covid-dades-simple.csv").read_text()
    return corona_file

def get_lines(contents:str) -> list[str]:
    pass

def get_column(lines: list[str]) -> list[int]:
    pass

def get_dosis(column: list[int]) -> int:
    pass

def get_sum(dosis: int) -> int:
    pass
