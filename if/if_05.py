import pprint
import random
import copy
import random

# piedra papel o tijeras
# input que escoge el jugador
# cpu escoge aleatoriamente
# anunciar el ganador 

option: list[str] = ["rock", "paper", "scissors"]
#usuario escoge

usr_hand: str = input("escoge : rock , paper, scissors: ")

#cpu escoge

cpu_hand: str = random.choice(option)

if usr_hand == "rock" and cpu_hand == "paper":
    print("lose")
elif usr_hand == "rock"  and cpu_hand == "scissors":
    print("win")
elif usr_hand == "paper" and cpu_hand == "scissors":
    print("lose")
elif usr_hand == "paper" and cpu_hand == "rock":
    print("win")
elif usr_hand == "scissors" and cpu_hand == "rock":
    print("lose")
elif usr_hand == "scissors" and cpu_hand == "paper":
    print("win")
else:
    print("draw")
