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
    print("Are you ready for some Formula One questions?\n")
    print("""Select either Start Quiz or Rules in the meny below by  
    following the instructions underneath the meny options.""")
    print("""
    -        Start Quiz        -
    -           Rules          -

    Instructions: 
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
                    get_username()
                    break 
                elif option == 'R': 
                    game_rules()
                    break
    except Exception: 
        clear()
        print("""Wrong...! You did not type 's or S' or 'r or R' to choose 
        either Start Quiz or see the Rules. Please type the following to 
        continue: 's or S' for Start Quiz or 'r or R' to see the Rules.\n""")
        user_game_meny()


def game_rules(): 
    """
    To display the game rules for the user 
    """
    clear()
    print("Welcome to Game Rules!")
    print("""
        This quiz consists of 12 questions, and the answer for each question
        will be either one of two options that are displayed underneath.
        you will have to Type either '1' or '2' to select the answer you
        think is the correct one and press Enter. The quiz will countinue
        until all 12 questions has been asked. Good luck!\n""")
    print("Type 'm or M' to return to the Menu.")
    try: 
        while True: 
            back_to_menu = input("")
            back_to_menu = back_to_menu.upper()
            if back_to_menu not in ["M"]: 
                raise Exception
            else: 
                main_meny_options()
    except Exception: 
        clear()
        print("Did you really press 'm or M'? Try again!")
        time.sleep(2)
        game_rules()
                

def get_username(): 
    """
    Get the users name to make the Quiz more personal for the player 
    """
    clear()
    print("""Before we can start the quiz for you, you need a username!\n
    You can choose anything you want but it can't be longer then 
    14 characters and it has to be in letters 
    (not numbers or special characters).\n""")
    try: 
        while True: 
            user_name = str(input("Write your username: \n"))
            if len(user_name) <= 14 and user_name.isalpha(): 
                print(f"Thank you {user_name}! One step closer to start the quiz.")
                return user_name
            else: 
                print("Not longer then 14 characters, written with numbers or special characters!\n")
    except Exception: 
        get_username()


def start_random_quiz(): 
    """
    Start the quiz and generate a random question from formula_questions 
    """
    previous_question = []
    quiz_question = []
    while quiz_question < 12: 
        x = random.randint(0, (len(formula_questions) -1))
        if x not in previous_question: 
            previous_question.append(x)
            quiz_question.append(formula_questions[x])
    return quiz_question


def user_question():
    """
    Displays the random generated question for the user 
    """
    i = 0 
    point = 0 
    while i < 12: 
        print(quiz_question[i]["question"])
        print(f"1 - {quiz_question[i]['options'][0]}")
        print(f"2 - {quiz_question[i]['options'][1]}")
        
        correct_answer = correct_answer_question(quiz_question[i])
        user_answer = user_answer_input()
        if user_answer == correct_answer: 
            point += 1 
            print(f"Correct! Well done. You scored {point} points!")
        else: 
            print("Oh no you guessed wrong. Better luck in the next question!")
        time.sleep(4)
        i = i + 1 
    return point 


def correct_answer_question(quiz_question):
    """
    Checks for the correct answer out of the two options for each question 
    """ 
    if quiz_question['correct'] == quiz_question['options'][0]: 
        return 1
    elif quiz_question['correct'] == quiz_question['options'][1]: 
        return 2


















game_start()