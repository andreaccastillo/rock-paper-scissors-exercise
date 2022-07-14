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


#DISPLAYING RESULTS
