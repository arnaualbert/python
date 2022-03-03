import random
import sys


def get_comand_line(commands: list[str]):

    proram_name: str = commands[0]
    program_paramters: list[str] = commands[1:]

    assert len(program_paramters) >= 1

    opcion: list[str] = program_paramters

    return opcion

def escoger_opcion(opcion):

    eleccion: str = random.choice(opcion)

    return eleccion


opcion: list[str] = get_comand_line(sys.argv)

print(escoger_opcion(opcion))