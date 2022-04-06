# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from questions import formula_questions
import os 
import time 
import random 
import pyfiglet


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
    f1_text = pyfiglet.figlet_format("F 1  Q U I Z", font = "3-d")
    print(f1_text)
    user_game_meny()


def user_game_meny(): 
    """
    Game meny with the two options of either start the quiz or watch game 
    rules for the quiz
    """ 
    print("Hello player! Are you ready for some Formula One questions?")
    print("""
    -        Start Quiz        -
    -        Quiz Rules        -
    Type 's or S' to start the quiz, type 'r or R' to watch Quiz Rules.""")
