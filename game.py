# this is the "game.py" file...

import random
from xml.sax.xmlreader import InputSource


print("Welcome to my Rock, Paper, Scissors game!")

#USER INPUTS

user_choice = input( "Please make a selection ( 'rock', 'paper', 'scissors'):")
user_choice = user_choice.lower()
valid_options = ["rock", "paper", "scissors"]

# You chose rock
print (f"You chose: '{user_choice}' ")

#VALIDATE USER INPUTS

#breakpoint()

if user_choice in valid_options:
        #COMPUTER CHOICE
        #import random
        valid_options = ["rock", "paper", "scissors"]
        Computer_choice = random.choice(valid_options)
        print(f"Computer chose:", Computer_choice)

        #DETERMINING THE WINNER
        #adapated from code shared in slack by Bonnie:
        #https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239
        if user_choice == Computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if Computer_choice == "scissors":
                print("Rock crushes scissors. You win!")
            else:
                print("Paper covers rock. You lose.")
        elif user_choice == "paper":
            if Computer_choice == "rock":
                print("Paper covers rock. You win!")
            else:
                print("Scissors cuts paper. You lose.")
        elif user_choice == "scissors":
            if Computer_choice == "paper":
                print("Scissors cuts paper. You win!")
            else:
                print("Rock crushes scissors. You lose.")

        # DISPLAYING RESULTS

else:
    print("Invalid, Try Again!")

print("Play Again, Soon!")
