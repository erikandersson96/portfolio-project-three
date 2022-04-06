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
    print("Hello player! Welcome to this Formula One Quiz!\n")
    f1_text = pyfiglet.figlet_format("F 1  Q U I Z", font = "3-d")
    print(f1_text)
    user_game_meny()


def user_game_meny(): 
    """
    Game meny with the two options of either start the quiz or watch game 
    rules for the quiz
    """ 
    print("Are you ready for some Formula One questions?")
    print("""
    -        Start Quiz        -
    -           Rules          -

    Type 's or S' to start the quiz, type 'r or R' to see the Rules.\n""")
    main_meny_options()


def main_meny_options(): 
    """
    Main meny to check which option the user selected between Start Quiz 
    or Rules 
    """
    try: 
        while True: 
            option = input("")
            option = option.upper()
            if option not in ["S", "R"]: 
                raise Exception
            else: 
                if option == 'S':
                    print("Start Quiz")
                    break 
                elif option == 'R': 
                    print("Rules")
                    break
    except Exception: 
        clear()
        print("""Wrong... You did not type 's or S' or 'r or R' to choose 
        either Start Quiz or see the Rules. Please type the following to 
        continue: 's or S' for Start Quiz or 'r or R' to see the Rules.\n""")
        user_game_meny()


game_start()