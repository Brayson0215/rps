







import random


# define the Compuer choice function to choose all rock, paper, scissors

def RPS():
    computer_choice = random.randint(1 ,3)  # we wanna give com. three choices
    if computer_choice ==1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()


name = input("enter the name")
while name.isdigit() == True or len(name) < 5:
    name = input("please enter valid name")
print("Name:", name)
age = input("enter the age")
while age.isalpha() == True or int(age) < 3:
    age = input("please enter your age")
print("Age", age)

password = input("enter the password")
while True:
    if password == 'Brayson':
        print("Correct passwworsd")
        break
    else:
        password = input("enter the correct password")

global score
score = 0


# define when computer choose rock
def computer_choice_rock():
    global score

    user_choice = input("1 rock, 2 paper, 3 scissors: ")
    if user_choice == "1":
        print("DRAW. YOU CHOOSE ROCK AND THE COMPUTER CHOSE ROCK")
        try_again()
    if user_choice == "2":
        print("YOU WIN. YOU CHOOSE PAPER AND THE COMPUTER CHOSE ROCK")

        score = score + 1
        try_again()

    if user_choice == "3":
        print("YOU LOOSE. YOU CHOOSE SCISSORS AND THE COMPUTER CHOSE ROCK")
        try_again()
    else:
        print("Try again")
        computer_choice_rock()  # while user put invalid option


# define when computer choose paper
def computer_choice_paper():
    global score

    user_choice = input("1 rock, 2 paper, 3 scissors: ")
    if user_choice == "1":
        print("YOU LOOSE. YOU CHOOSE  AND THE COMPUTER CHOSE PAPER")
        try_again()
    if user_choice == "2":
        print("DRAW. YOU CHOOSE PAPER AND THE COMPUTER CHOSE PAPER")
        try_again()
    if user_choice == "3":
        print("YOU WIN. YOU CHOOSE SCISSORS AND THE COMPUTER CHOSE PAPER")

        score = score + 1
        try_again()

    else:
        print("Try again")
        computer_choice_paper()  # while user put invalid option


def computer_choice_scissors():
    global score

    user_choice = input("1 rock, 2 paper, 3 scissors: ")
    if user_choice == "1":
        print("YOU WIN. YOU CHOOSE ROCK AND THE COMPUTER CHOSE SCISSORS")

        score = score + 1
        try_again()

    if user_choice == "2":
        print("YOU loose. YOU CHOOSE PAPER AND THE COMPUTER CHOSE SCISSORS")
        try_again()
    if user_choice == "3":
        print("DRAW. YOU CHOOSE SCISSORS AND THE COMPUTER CHOSE SCISSORS")
        try_again()
    else:
        print("Try again")
        computer_choice_scissors()  # while user put invalid option
    print("score", score)



# tryagain
def try_again():
    choice = input("TRY AGAIN OR NOT? y/n")
    global score
    if choice == "y" or choice == "yes" or choice == "Y":
        RPS()
    elif choice == "n":
        print("thanks for playing")
        print("Your Final score is ", score)
        quit()
    else:
        print("try again")
        try_again()


RPS()






