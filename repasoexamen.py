# top down y bottom up
# agrupar en funciones 

import pprint
import random
import copy

# piedra papel o tijeras
# input que escoge el jugador
# cpu escoge aleatoriamente
# anunciar el ganador

# lista de opciones

option: list[str] = ["rock", "paper", "scissors"]
draw = 0
# usuario escoge

def get_usrhand():
    usr_hand: str = input("escoge : rock , paper, scissors: ")
    return usr_hand



# cpu escoge

def get_cpuhand(option):
    cpu_hand: str = random.choice(option)
    print(f"la cpu escoge : {cpu_hand}")
    return cpu_hand


def get_result(draw):
    if usr_hand == "rock" and cpu_hand == "paper":
        draw - 1
    elif usr_hand == "rock" and cpu_hand == "scissors":
        draw + 1
    elif usr_hand == "paper" and cpu_hand == "scissors":
        draw - 1
    elif usr_hand == "paper" and cpu_hand == "rock":
        draw + 1
    elif usr_hand == "scissors" and cpu_hand == "rock":
        draw - 1
    elif usr_hand == "scissors" and cpu_hand == "paper":
        draw + 1
    else:
        draw + 2

def get_sp(draw):
    if draw == -1:
        print("loser")
    elif draw == 1:
        print("winner")
    elif draw == 2:
        print("draw")

usr_hand = get_usrhand()
cpu_hand = get_cpuhand(option)
get_result(draw)
get_sp(draw)
