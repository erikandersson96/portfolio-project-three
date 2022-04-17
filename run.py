"""
Python 3 project.
Portfolio Project 3: Formula One Quiz.
Developed and written by Erik Andersson, April 2022.
My code is custom written to fit mock terminal on Heroku,
with 80 characters wide and 24 rows high.
"""
# These are python libraries and imports from those libraries
# from questions import formula_questions is to import questions
from questions import formula_questions
import os
import time
import random
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# Credential values the same as Code Institute Love Sandwiches project
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('formula_one_quiz')


def clear():
    """
    This function adds the ability to clear the terminal to get more space
    in some functions
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_start():
    """
    Start up the game, welcome message and start up the meny with options
    """
    clear()
    print("")
    f1_text = pyfiglet.figlet_format("F 1  Q U I Z", font="3-d")
    print(f1_text)
    user_game_menu()


def user_game_menu():
    """
    Game meny with three options of either start the quiz, see leaderboard
    or watch game rules for the quiz
    """
    print("Are you ready for some Formula One questions?\n")
    print("Select either Start Quiz, Leaderboard or Game Rules in the menu")
    print("below by following the instructions underneath the menu options.")
    print("""
    -        Start Quiz        -
    -        Leaderboard       -
    -        Game Rules        -\n""")
    print("Instructions:")
    print("Type 's or S' to Start the Quiz, Type 'l or L' to see the")
    print("Leaderboard, Type 'r or R' to see the Game Rules.")
    main_menu_options()


def main_menu_options():
    """
    Main meny to check which option the user selected between Start Quiz
    or Rules
    """
    try:
        while True:
            option = input("\n").upper()
            if option not in ["S", "L", "R"]:
                raise ValueError
            else:
                if option == 'S':
                    main()
                    break
                elif option == 'L':
                    leaderboard()
                    break
                elif option == 'R':
                    game_rules()
                    break
    except ValueError:
        clear()
        print("Wrong...! You did not type 's or S', 'l or L' or 'r or R'")
        print("to choose either Start Quiz, Leaderboard or see the Rules.")
        print("Please type the following to continue: 's or S' for ")
        print("Start Quiz,'l or L' for Leaderboard or")
        print("'r or R' to see the Rules.\n")
        user_game_menu()


def game_rules():
    """
    Display the game rules of Formula One Quiz to the user
    """
    clear()
    print("Welcome to Game Rules!")
    print("""
        This quiz consists of 6 or 12 questions, and the answer for each
        question will be either one of two options that are displayed
        underneath. You will have to Type either '1' or '2' to select
        the answer you think is the correct one and press Enter.
        The quiz will countinue until all questions has been played
        for the selected amount of questions. Good luck!\n""")
    print("Type 'm or M' to return to the Menu.")
    try:
        while True:
            back_to_menu = input("\n").upper()
            if back_to_menu not in ["M"]:
                raise ValueError
            else:
                clear()
                user_game_menu()
    except ValueError:
        clear()
        print("Did you really press 'm or M'? Try again!")
        time.sleep(3)
        game_rules()


def leaderboard():
    """
    Leaderboard() is used display the leaderboard rankings for the user
    """
    clear()
    print("Loading...")
    time.sleep(2)
    clear()
    print("******* Leaderboard *******")
    print("")
    leader_six = get_score_from_sheet(6)
    leader_twelve = get_score_from_sheet(12)
    print("6 Questions:\n")
    if len(leader_six) < 3:
        leaders = len(leader_six)
    else:
        leaders = 3
    for i in range(leaders):
        print(f"{i + 1}) {leader_six[i][0]} {leader_six[i][1]} Points\n")
    print("")
    print("12 Questions:\n")
    if len(leader_twelve) < 3:
        leaders = len(leader_twelve)
    else:
        leaders = 3
    for i in range(leaders):
        print(f"{i + 1}) {leader_twelve[i][0]} {leader_twelve[i][1]} Points\n")
    print("")
    print("")
    print("Return to menu, Type 'm or M'")
    try:
        while True:
            back_to_menu = input("\n").upper()
            if back_to_menu not in ["M"]:
                raise ValueError
            else:
                clear()
                user_game_menu()
    except ValueError:
        clear()
        print("Did you really press 'm or M'? Try again!")
        time.sleep(3)
        leaderboard()


def get_username():
    """
    Get the users name to make the Quiz more personal for the player
    and later add it to the leaderboard worksheet
    """
    clear()
    print("""Before we can start the quiz for you, you need a username!\n
    You can choose anything you want but it can't be longer then
    10 characters and it has to be in letters
    (not numbers or special characters).\n""")
    try:
        while True:
            user_name = str(input("Write your username:\n"))
            if len(user_name) <= 10 and user_name.isalpha():
                clear()
                print(f"Thank you {user_name}!")
                return user_name
            else:
                print("")
                print("Not longer then 10 characters.")
                print("Written with numbers or special characters.")
                print("Try again!\n")
    except ValueError:
        get_username()


def how_many_questions():
    """
    User get to choose to play either 6 or 12 questions out of 12
    questions
    """
    print("")
    print("Loading quiz...")
    time.sleep(2.5)
    clear()
    print("How many questions would you like to play?")
    while True:
        try:
            amount_questions = int(input("6 or 12:\n"))
            if amount_questions not in [6, 12]:
                raise ValueError
            else:
                clear()
                return amount_questions
        except ValueError:
            clear()
            print("You didn't Type in '6 or 12'! Please choose only one.")


def get_score_from_sheet(which_quiz):
    """
    Import all data from both worksheets 6 and 12 and organize them in order
    from top to bottom for the leaderboard
    """
    if which_quiz == 6:
        googlesheet = SHEET.worksheet('questions-6')
    elif which_quiz == 12:
        googlesheet = SHEET.worksheet('questions-12')
    googlesheet.sort((2, "des"))
    googlesheet_values = googlesheet.get_all_values()
    return googlesheet_values


def start_random_quiz(amount_questions):
    """
    Generate random question for the user and makes sure that the questions
    doesn't get repeated for the user
    """
    quiz_question = []
    full_questions = formula_questions.copy()
    for _ in range(amount_questions):
        q_num = random.randint(0, (len(full_questions)-1))
        quiz_question.append(full_questions.pop(q_num))
    return quiz_question


def user_question(quiz_question, amount_questions):
    """
    Display the random generated question to the user from
    start_random_quiz function
    """
    i = 0
    point = 0
    question = 0
    while i < amount_questions:
        question += 1
        print(f"Question {question}/{amount_questions}.\n")
        print(quiz_question[i]["question"])
        print(f"1 - {quiz_question[i]['options'][0]}")
        print(f"2 - {quiz_question[i]['options'][1]}")
        print("")
        correct_answer = correct_answer_question(quiz_question[i])
        user_answer = user_answer_input()
        if user_answer == correct_answer:
            point += 1
            print("Correct! Well done. You scored 1 point!\n")
            print(f"Your current score: {point} points!\n")
            time.sleep(2)
        else:
            print("Oh no you guessed wrong. 0 points for this question.")
            print("Better luck in the next question!\n")
            print(f"You have: {point} points this far!\n")
            time.sleep(2)
        time.sleep(1)
        i += 1
        clear()
    return point


def correct_answer_question(quiz_question):
    """
    Checks for the correct answer out of the two options for each question
    """
    if quiz_question['correct'] == quiz_question['options'][0]:
        return 1
    elif quiz_question['correct'] == quiz_question['options'][1]:
        return 2


def user_answer_input():
    """
    Here it checks what the user inputted as answer between the two options and
    if it is a valid input
    """
    print("What do you think is the correct answer?")
    while True:
        try:
            user_answer = input("1 or 2:\n")
            user_answer = int(user_answer)
            print("")
            print(f"Your answer is {int(user_answer)}.\n")
            if user_answer not in [1, 2]:
                raise ValueError
            else:
                return user_answer
        except ValueError:
            print("")
            print("Only enter either '1 or 2'. You entered something else... ")


def user_to_leaderboard(amount_questions, user_name, point):
    """
    This function adds all data about username, total points to the correct
    game mode, either 6 or 12 questions
    """
    if amount_questions == 6:
        user_point_six = SHEET.worksheet('questions-6')
        user_point_six.append_row([user_name, point])
    elif amount_questions == 12:
        user_point_twelve = SHEET.worksheet('questions-12')
        user_point_twelve.append_row([user_name, point])


def end_message(user_name, point):
    """
    End message with information about the users name and point that the user
    scored
    """
    clear()
    print("Well done! I hope your Formula One knowledge got a little")
    print("better with this quiz.\n")
    print(f"{user_name} you scored at total of {point} points!\n")
    input("Please press enter to continue...\n")


def user_choice_exit():
    """
    Gives the user a choice when end_message is showing after all questions to
    restart the quiz or exit the program
    """
    clear()
    print("Do you want to play again?")
    print("Type Y (yes) or N (no) to exit the program.\n")
    while True:
        try:
            user_choice = str(input("Y or N:\n")).upper()
            if user_choice not in ["Y", "N"]:
                raise ValueError
            else:
                if user_choice == 'Y':
                    game_start()
                elif user_choice == 'N':
                    exit(0)
        except ValueError:
            print("")
            print("You did not Type 'y or Y' for yes to play the quiz again")
            print("or 'n or N' for no to exit the program.")
            print("You typed something else, try again.\n")


def main():
    """
    Main holds all function calls
    """
    user_name = get_username()
    amount_questions = how_many_questions()
    quiz_question = start_random_quiz(amount_questions)
    point = user_question(quiz_question, amount_questions)
    end_message(user_name, point)
    user_to_leaderboard(amount_questions, user_name, point)
    user_choice_exit()


if __name__ == "__main__":
    game_start()
