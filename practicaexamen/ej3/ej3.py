# import psutil
import os
from pathlib import Path
# def get_espacio(saber_espacio: Path):

#    total = os.stat(saber_espacio).st_size
#     sub_dirs: list[Path] = Path(saber_espacio).rglob('*')
    # sub_dirs: list[Path] = Path('/home').glob('*')
    # total: Path = Path(saber_espacio).stat().st_size
    # sub_dirs: list[Path] = Path(saber_espacio).glob('*')
    # for dir in sub_dirs:
    #     x: int = dir.stat().st_size
    # total: Path = Path(x).stat().st_size


# print(get_espacio('/home'))

# sub_dirs: list[Path] = Path('/home').glob('*')
# dir: Path = Path('/home').stat().st_size
# print(dir)

sub_dirs: list[Path] = Path('/home').glob('*')
for dir in sub_dirs:
    x: int = dir.stat().st_size
print(x)