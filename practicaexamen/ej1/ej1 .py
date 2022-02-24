
from importlib.resources import path
from pathlib import Path
import shutil
import engine

def get_txt(txt_file: Path, txt_template: Path):

    inv: str = Path("friends.txt").read_text()
    names_list: list[str] = inv.split(",")
    for name in names_list:
        tmp_dir: Path = Path(".")
        var_dict: dict = {"name": name}
        invitation: str = engine.fill_template(tmp_dir,txt_template,var_dict)
        invitation_new : str = f'{name}.txt'
        ruta_invitation : Path = Path(invitation_new)
        ruta_invitation.write_text(invitation)



get_txt("friends.txt","invitation.txt") 

