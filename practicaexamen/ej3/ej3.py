import sys
import os
from pathlib import Path


def get_espacio(dir, glob) -> int:

        dirpath:       Path       = Path(dir)
        path_list:     list[Path] = list(dirpath.rglob(glob))
        filepath_list: list[Path] = [path for path in path_list if path.is_file()]

        stat_list : list[os.stat_result] = [filepath.stat() for filepath in filepath_list]
        size_list:  list[int]         = [stat.st_size for stat in stat_list]
        total_size: int               = sum(size_list)

        return total_size

#    total = os.stat(saber_espacio).st_size
#    sub_dirs: list[Path] = Path(saber_espacio).rglob('*')
#    sub_dirs: list[Path] = Path('/home').glob('*')
#    total: Path = Path(saber_espacio).stat().st_size
#    sub_dirs: list[Path] = Path(saber_espacio).glob('*')
#    for dir in sub_dirs:
#         x: int = dir.stat().st_size
#         dir: Path = Path(x).stat().st_size
def get_command_line(commands: list[str]) -> tuple[str,str]:

        program_name: str  = commands[0]
        program_parameters: list[str] = commands[1:]

        dir, glob = program_parameters
        return dir, glob
 
dir, glob = get_command_line(sys.argv)
print(get_espacio(dir, glob))

# sub_dirs: list[Path] = Path('/home').glob('*')
# dir: Path = Path('/home').stat().st_size
# print(dir)

# sub_dirs: list[Path] = Path('/home').glob('*')
# for dir in sub_dirs:
#     x: int = dir.stat().st_size
# print(x)