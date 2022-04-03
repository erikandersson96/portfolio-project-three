# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from questions import formula_questions
import os 
import time 
import random 


def clear(): 
    """
    This function adds the ability to clear the terminal to get more space 
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_start(): 
    """
    Start up the game, welcome message and start up the meny with options
    """
    clear()
    print("Hello there! Welcome to this Formula One Quiz!")
    print("""

        #########     ##            ##         ##      ##   ##    ########
        ##          ####         ##    ##      ##      ##   ##         ##
        ##            ##        ##      ##     ##      ##   ##        ##
        #######       ##       ##        ##    ##      ##   ##       ##
        ##            ##        ##      ##     ##      ##   ##      ##
        ##            ##         ##    ##      ##      ##   ##     ##
        ##          ######         #######        ####      ##    ########
    """)