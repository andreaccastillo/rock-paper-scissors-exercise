# this is the "game.py" file...

import random
from xml.sax.xmlreader import InputSource

print("Rock, Paper, Scissors, Shoot!")



#USER INPUTS

user_choice = input( "Please make a selection ( 'rock', 'paper', 'scissors'):")

# You chose rock
print (f"You chose: '{user_choice}' ")

#VALIDATE USER INPUTS


#COMPUTER CHOICE

#import random
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print(f"computer chose:", computer_choice)

#DETERMINING THE WINNER
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

#DISPLAYING RESULTS
