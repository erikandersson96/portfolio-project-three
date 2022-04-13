# Formula One Quiz 

Formula One Quiz is a quiz built with Python. The quiz has 12 questions and for every question there is 2 options for the answer but only 1 is correct. 
The questions are all subjected around Formula One, both about historical moments from the very start until the 2020 season. So if you want to test your knowledge 
in Formula One, play the quiz. 

**Remember that all links in this Readme does not open in a new tab. They open in the same window.** 

To play the quiz you can click this [link](link). 

![Screenshot of Welcome message Formula One Quiz](/assets/images/welcome.png)


---
## Portfolio Project Three 

### Intention 

This website is a fictional website for the purpose of my Third Portfolio Project for Code Institute’s Full Stack Software Development Course. I created this website with the knowledge I gained from the `Python` module.

The main goal of this project was to test my new knowledge in Python. I decided to create a 12 question Quiz Game about Formula One. 

##### Features I aimed to achieve with this project:

* To make the game `easy` to understand for the user. 
* Make sure that the game has good `instructions` through out the whole game so the user doesn't get confuesed. 
* To get people more educated about the sport of Formula One. 


## Table of Contents

* [UX](#ux) 
  * [Strategy](#strategy)
  * [Visitor Goals](#visitor-goals) 
  * [User Stories](#user-stories) 

* [Logic](#logic) 
  * [Flow Diagram](#flow-diagram) 
  * [Comparison](#comparison) 

* [Existing Features](#existing-features)
  * [Start Screen]()
  * [Leaderboard]()
  * [Game Rules]()
  * [Username]()
  * [Question Selection]()
  * [Questions]()
  * [End Message]()
  * [Play Again]()

* [Testing](#testing)
  * [Manual Testing](#manual-testing)
    * [Bugs & Solutions](#bugs--solutions)
  * [Validation](#validation)

* [Python Libraries](#python-libraries)

* [Credits](#credits)

* [Deployment](#deployment)

* [Support](#support) 


---
## UX 

#### Strategy 

This Formula One Quiz was created with the intention to test peoples knowledge in the sport. A game that people can share among their friends and family to challenge each other's knowledge. 
Since the whole game is operated entirely in the terminal with no colorful graphics the user can then try to imagine how the different drivers, team's and situations would look like 
for that given time. 

#### Visitor Goals 

* To create a simple and fun Quiz for everyone above 14+ years old. 
* To give the user a simple navigation at the main menu with simple instructions. 
* To always provide the user with all the information about which question that is displayed of the amount that the user choose (6 or 12) 
and count how many points the user has scored for each question. 

#### User Stories 

* **A user's perspective:** I want to easily understand the purpose of the website.  
* **A user's perspective:** I want the quiz to have clear instructions about how the game works. 
* **A user's perspective:** I want the game to always provide me with information about how many questions I have played and have left, also how many points I have scored. 


---
## Logic 

#### Flow Diagram 

Before I started to write any code for this project I made sure to create an easy and straightforward `Flow Diagram` with all the logic for this Quiz. The `Flow Diagram` was created with the use of 
[Lucid Chart](https://www.lucidchart.com/pages/) (link). I used the free version that is available for anyone that register an acount at their website. My `Flow Diagram` is demonstrated below. 

![Screenshot of my flow diagram](/assets/images/) ADD FINAL FLOW DIAGRAM!


---
## Existing Features

#### Start Screen 

When the program starts the user will get a `Welcome message` including a `"Banner"` and a menu of three different options `Start Quiz | Leaderboard | Game Rules`. Underneath the menu the user can find the instructions about how to select the different options from the menu. See the screenshot below:

![Screenshot of start screen](/assets/images/welcome.png)

If the user doesn't care to follow the instructions or accidentally types the wrong character instead a message will appear to inform the user that he or she has to try again with a valid input. See the screenshot below:  

![Screenshot of error message wrong input start screen](/assets/images/welcome-wrong.png)

#### Leaderboard & Game Rules

When the user selects the `Leaderboard` option he or she will see a leaderboard containing the top 3 finishers of the two different question selections either 6 or 12. When the user want's to exit the leaderboard an get back to the menu there is instructions below that explains this. See the screenshot below:

![Screenshot of leaderboard](/assets/images/)

When the user selects the `Game Rules` option he or she will first get a message that welcomes the user to the Game Rules, after that all of the Game Rules will be displayed. When the user want to exit the Game Rules and get back to the menu there is instructions below that explains this. See the screenshot below:

![Screenshot of Game Rules](/assets/images/rules.png)

When the user want to exit the `Leaderboard or Game Rules` to get back to the menu and accidentally types the wrong character instead of `m or M` a message will appear to inform the user that he or she has to try again with a valid input. See the screenshot below:

![Screenshot of exit leaderboard or game rules](/assets/images/rules-wrong.png)

#### Username 

When the user selects `Start Quiz` to start the quiz a message will appear that says that the user needs to fill in a username, some instructions underneath the first message will inform the user that the username can't be any longer then 10 characters, it can't inculde numbers or special characters. See the screenshot below:

![Screenshot of type in username](/assets/images/username.png)

If the user selected a `valid username` this message will appear: 

![Screenshot of type in username](/assets/images/username-correct.png)

When the user types in his or her username and accidentally types anything else then alphabetics a message will appear to inform the user that he or she has to try again with a valid input. See the screenshot below:

![Screenshot of error when type in username](/assets/images/username-wrong.png)

#### Question Selection 

After the user has selected a valid `username` he or she wiill be asked how many questions to play either `6 or 12`. See the screenshot below:

![Screenshot of question selection](/assets/images/amount-questions.png)

If the user types an invalid number or character not `6 or 12` a message will appear with instructions of how to continue. See the screenshot below:

![Screenshot of error message question selection](/assets/images/amount-wrong.png)

#### Questions 

The `questions` in the Quiz will be displayed to the user right after that the user has selected a valid input between `6 or 12` for the question selection, the user can choose between two options for each question, but only one is the correct answer. See the screenshot below:

![Screenshot of question](/assets/images/question.png)

If the user inputs the correct answer of `either 1 or 2` this message will appear. See the screenshot below:

![Screenshot of correct answer for question](/assets/images/answer-correct.png) 

If the user inputs the wrong answer of `either 1 or 2` this message will appear. See the screenshot below:

![Screenshot of wrong answer for question](/assets/images/answer-wrong.png)

When the user `answers` the question he or she can only input either `1 or 2` as a valid answer for the question, if the user inputs anything else then one of these a message will appear with instructions of how to continue. See the screenshot below:

![Screenshot of error message question](/assets/images/question-wrong.png)

#### End Message

When the user has `completed` all questions of the selected amount `6 or 12 questions` a result message will appear to inform the user about how many points he or she got. The user will see underneath `Please press enter to continue...`. See the screenshot below:

![Screenshot of end message](/assets/images/end-message.png)

#### Play Again 

When the user has pressed enter a message will appear with a question to the user that ask the user if he or she wants to play again or quit the quiz. If the user choose to play again 
`Y (yes)` he or she will be directed back to the menu, if the user choose `N (no)` the quiz will exit. See the screenshot below:

![Screenshot of play again, yes or no](/assets/images/play-again.png)

If the user input something else then `Y or N` a message will appear to inform the user that he or she needs to try again with a valid option. See the screenshot below:

![Screenshot of error message play again, yes or no](/assets/images/play-again-error.png)


---
## Testing

### Manual Testing 

#### Bugs that are fixed

* **Bug 1:** 
Write wrong character option when user answer a question. 
When playing the quiz, if the user inputs a wrong character instead of '1 or 2' which are the only accepted answers the 
user will get a warning that says `"Only enter eiter '1 or 2'. You entered something else. "` to let the user know that 
he or she didn't input a valid value. But if the user then tries to choose either '1 or 2' the program will repeat the same 
issue and won't let the user input the valid value to countinue the quiz. 

**Screenshot:**

![Screenshot bug 1](/assets/images/bug1.png) 


* **Bug 2:** 
When exit the game Rules. 
When the user is finsihed reading the game Rules for the quiz, he or she is supposed to Type 'm or M' and then press enter to 
get back to the Meny. But when the user does this the program doesn't respond correctly before the user tries for the second time. 
When the user types 'm or M' and press enter, first nothing happens so when the user then repeat's the process a second time the program 
responds and get the user back to the Meny but it gives the user a error message above the Meny that the user didn't use the correct 
command. So the program gets quite confusing for the user when this bug happens. 

**Screenshot:** 

![Screenshot bug 1](/assets/images/bug2.png)


* **Bug 3:**
End message doesn't show up. 
When the user has answered all of the selected questions (6 or 12). The end message should show up with: 
`Well done! I hope your Formula One knowledge got a little better with this quiz.`, `{user_name} you scored at total of {point} points!`.
`{user_name}` and `{points}` is used in an f-string to input the user name of the user and the total points that the user scored. 
But the end message does not show up at all, the Quiz just goes back to the the meny with the same error above the meny as with **Bug 2**. 

**Screenshot:**

![Screenshot bug 1](/assets/images/bug2.png)


### Validation


### User Story Testing 

To meet the expectations in the user stories. I have tested my python project for each of them.

1. **Goal** 
* A user's perspective: I want to easily understand the purpose of the website. 

**Result**
* By presenting the game with `"F1 QUIZ"` first and a welcome message that explains that says `"Welcome to this Formula One Quiz!"`, so the user quickly understand the purpose of this website (python project). 

2. **Goal**
* A user's perspective: I want the quiz to have clear instructions about how the game works.

**Result**
* By always presenting instructions below each step the user takes in the game. 

3. **Goal**
* A user's perspective: I want the game to always provide me with information about how many questions I have played and have left, also how many points I have scored.

**Result**
* By adding the functionality to see which question of the selected amount the user is on right above each question. When the user has answered a question and if the user is correct the total points scored will be displayed underneath, but also when the game is finished. 

## Python Libraries 

**Python libraries used for this project:** 

* **Os:** I choose to import this one so that I could enable the possibility for me to create a function that works as `"clear()"`, so I could call it within other functions so the terminal clears other text that were displayed before. The same principle is used when using the terminal in other situations and you want to clear out all unnecessary text so you get a cleaner look. 
* **Time:** I choose to import time to be able to set time delays `(time.sleep(seconds))` within certain functions so the Quiz doesn't executes to fast for the user to be able read the information.  
* **Random:** I had to import random in order for me to generate a random order of the questions for the user. 
This Formula One Quiz was created with the intention to test peoples knowledge in the sport. A game that people can share among their friends and family to challenge each other's knowledge. 
* **Pyfiglet:** I choose to import [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) (link) so I could display `"F1 QUIZ"` in a 3d look without the need to create it myself. Take a look at their website to get all of the instructions to how you can implement it your self to your next python project. 


---
## Credits


---
## Deployment 

**GitHub:**

I frequently used `commit` throughout the whole project, this is the commands used in the terminal: 

* `git add .` (This command is used for adding files to the staging area before committing).
* `git commit -m “commit message here..”` (This is used to label the commit changes made to the local repository).
* `git push` (This command is used to push all changes to the Github repository). 

This is all done to prevent any `data` loss in case Gitpod crashes.


#### GitHub & Gitpod 

For this project I used Code Institutes Python template that can be found [here](https://github.com/Code-Institute-Org/python-essentials-template) (link). 

**Steps to create a new repository in Github:**

1. Sign in or sign up to [GitHub](https://github.com) (link). 
1. When you have done that, you will see `"new"` up in the left corner. 
**Like this:**
![Screenshot new repository button github](/assets/images/github.png)
1. Select in the dropdown menu under `Repository template` if you for example would like to use the template provided by `Code Institute` that I did for this project. If you don't see it in the dropdown menu click this [link](https://github.com/Code-Institute-Org/python-essentials-template) to get to the one provided by `Code Institute` and click `Use this template` to the left of the green Gitpod button.
1. When you have done that, give the repository a name. Leave it public if you want anyone on the internet to see your repository (I always do). 
1. Click create repository. 
1. **Remember** to use the `commit` commands that I explained above so your hard work doesn't get lost if anything happens to Gitpod. 

#### Forking GitHub Repository

Forking a Github repository is the process of making a copy of someone else repository and add your own changes to it without changing the original, the original repository is known 
as "upstream repository". I will explain the process of forking down below: 

1. Go to the Github page that hosts the repository you wish to fork. 
1. In the top-right corner of the page there is a button that says `"Fork"`. 
1. Click this button. 
1. This creates a copy of that repository to your Github home page. You can submit and receive changes to your copy by using pull requests and/or syncing with the original upstream repository. 

This instructions were taken from [Github - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo). 

#### Cloning GitHub Repository

Cloning a repository inolves making a full copy of a repository on your local machine. This allows you to work on the code easier. Changes can be pushed back up to the Github site or changes from other sources pulled to your local copy. I will explain how to clone down below: 

1. Go to the repository page on Github. 
1. Above the file list click on the green button that says `"Code"`. 
1. You can choose to download a zip file of the repository, to unpack it on your local machine and open it in your IDE. 
1. Clone using HTTPS by copying the URL under the HTTPS tab. 
1. Open a terminal window, set current directory to the one you want to contain the clone from. 
1. Type `git clone` and paste the URL copied from the Github page. 
1. The repository clone will now be created on your machine. 

This instructions were taken from [Github - cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).


---
## Support 

I would like to give an extra `Thank you` to all the kind people I have around me that gave me support in all different ways. 

* **Code Institute** for their **Tutor** support. 
* My mentor [Benjamin Kavanagh](https://github.com/BAK2K3) for being a **Superior** mentor.
* **Google** for always clear things up.
* My lovely **Girlfriend** for always supporting and believing in me.

### RETURN TO THE [TOP](#formula-one-quiz)
