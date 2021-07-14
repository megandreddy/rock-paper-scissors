# game.py

import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

z = os.getenv("USER_NAME")


print(z)


#exit()

print("Rock, Paper, Scissors, Shoot!")






#
# ASK FOR A USER INPUT
# source: https://docs.python.org/3/library/functions.html#input
#s = input('--> ')

x = input("please choose one of 'rock', 'paper', 'scissors'; ")
print(x)

x = x.lower()
print(x)



# VALIDATE USER INPUT


if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()











# print("LATER MESSAGES")

print("USER CHOSE:", x)


# GENERATE A COMPUTER CHOICE
# source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#
# import random
#
# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))



valid_options = ["rock", "paper", "scissors"] # list

c = random.choice(valid_options)

print("COMPUTER CHOSE:", c)


# DETERMINE THE WINNER

#print("YOU WON!)

#print("COMPUTER WON!")

winners = {
    "rock": {
        "rock": None,
        "paper": "paper",
        "scissors": "rock",
    },
    "paper": {
        "rock": "paper",
        "paper": None,
        "scissors": "scissors",
    },
    "scissors": {
        "rock": "rock",
        "paper": "scissors",
        "scissors": None,
    }
}

winner = winners[x][c]
if winner == x:
    print("YOU WON! WOOHOO!")
elif winner == c:
    print("YOU LOST. NO WORRIES, PLAY AGAIN!")
else:
    print("TIE. PLAY AGAIN!")





