from random import randint


name=input("enter the name")
while name.isdigit()==True or len(name)<4:
    name=input("please enter the name")
print("Name:",name)
age=input("enter the age")
while age .isalpha()==True or int(age)<3:
    age=input("please enter the age")
print("Age:",age)
password=("apple")
password=input("enter the password")
if password==True:
    print("password",password)
global sum
sum=0

global score
score  =0


def gane():
    global score
    A = ["Rock", "Paper", "Scissors"]
    computer = A[randint(0, 2)]
    player = False

    while player == False:
        # print("LETS PLAY A GAME")

        player = input("Rock, Paper, Scissors")
        if player == computer:
            print("DRAW!")
        elif player == "Rock":
            if computer == "Paper":
                print("YOU LOSE TRY AGAIN")

            else:

                print("CONGRATULATION,YOU WIN \n ")
                score=score+1
        elif player == "Paper":
            if computer == "Scissors":
                print("YOU LOSE TRY AGAIN")
            else:

                print("CONGRATULATION,YOU WIN \n + score is:", sum)
                score=score+1
        elif player == "Scissors":
            if computer == "Rock":
                print("YOU LOSE TRY AGAIN")


        else:
            print("INVALID OPTION PLEASE ENTER THE CORRECT OPTION")
        player = False
        computer = A[randint(0, 2)]
        re = input("YOu want to play again y/n")
        if re == 'y':
            gane()
        else:
            menu()

def menu():
    print("1- playing \n 2- check score\n 3- quit")
    ch=input("enter choice")
    global score
    #while True:
    if ch=='1':
           print("LETS PLAY A GAME")
           gane()
    if ch=='2':
         print("SCORE YOU OBTAIN:",score)
         menu()

    if ch=='3':
        quit(0)

menu()