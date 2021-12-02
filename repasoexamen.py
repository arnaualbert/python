# top down y botton up, agrupar en funciones (al menos una pura)

import pprint
import random
import copy

# piedra papel o tijeras
# input que escoge el jugador
# cpu escoge aleatoriamente
# anunciar el ganador

# lista de opciones

option: list[str] = ["rock", "paper", "scissors"]

# usuario escoge

usr_hand: str = input("escoge : rock , paper, scissors: ")

# cpu escoge

cpu_hand: str = random.choice(option)
print(f"la cpu escoge : {cpu_hand}")

if usr_hand == "rock" and cpu_hand == "paper":
    print("lose")
elif usr_hand == "rock" and cpu_hand == "scissors":
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