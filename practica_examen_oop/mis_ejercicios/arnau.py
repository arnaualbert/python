from cgitb import reset
import re


class Player():

    def __init__(self,name: str,age: int,position: str, team: str):
        """_summary_

        Args:
            name (str): name of the player
            age (int): age of the player
            position (str): position of the player
            team (str): team of the player
        """
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    @classmethod
    def from_team(cls,coach: str):
        
        result: Player

        if coach == "pep":
            result = cls("Halaand",20,"striker","city")
        elif coach == "xavi":
            result = cls("ansu",19,"striker","barça")
        else:
            result = cls("nobody",21,"nothing","madriz")

        return result


def show_attributes(something) -> None:

    keys:   list = sorted(something.__dict__.keys())
    values: list = [something.__dict__[key] for key in keys]

    for key, value in zip(keys, values):
        print(f'{key}: {value}')

    print()

if __name__ == "__main__":
    halaand: Player = Player.from_team("pep")
    ansu: Player = Player.from_team("xavi")
    lolo: Player = Player.from_team("lolo")
    show_attributes(halaand)
    show_attributes(ansu)
    show_attributes(lolo)