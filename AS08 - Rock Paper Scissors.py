import random

choices = ["rock", "paper", "scissors"]

def game(c):
    choice = random.choice(choices)
    uc = str(input("Rock? Paper? Or Scissors? please enter one: "))

    if uc not in choices:
        print("Invalid input")

    elif uc == choice:
        print(f"Computer: {choice}, user: {uc}. It's a draw")

    elif (uc == "rock" and choice == "scissors") or (uc == "paper" and choice == "rock") or (uc == "scissors" and choice == "rock"):
        print(f"Computer: {choice}, user: {uc}. User wins")
    else:
        print(f"Computer: {choice}, user: {uc}. Computer wins")

while True:
    game(choices)
    again = str(input("If you would like to continue please enter 'y', if not enter 'n': "))
    if again == "n":
        break
