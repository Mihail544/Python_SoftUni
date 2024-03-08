import random

Round_Count = 0
Ai_Wins = 0
Player_Wins = 0


def Rock_Paper_Scissors():
    print(f"Here we are , round number {Round_Count}")
    choices = ["Rock", "Paper", "Scissors"]

    Ai_input = random.choice(choices)

    while True:
        Player_input = input("Rock , Paper or Scissors ? ").capitalize()
        if Player_input in choices:
            break
        else:
            pass

    if Player_input == Ai_input:
        print("AI:" + Ai_input)
        print("Player:" + Player_input)
        print("Tie!")

    elif Player_input == "Rock":
        if Ai_input == "Paper":
            print("You Lose ):")
            return False
        else:
            print("You Win :D")
            return True

    elif Player_input == "Paper":
        if Ai_input == "Scissors":
            print("You Lose ):")
            return False
        else:
            print("You Win :D")
            return True
    else:
        if Ai_input == "Rock":
            print("You Lose ):")
            return False
        else:
            print("You Win :D")
            return True


def Play_Again():
    while True:
        if Round_Count == 0:
            Round = input("Do you want to play a game ? Y/N ").capitalize()
        else:
            Round = input("Do you want to play again ? Y/N ").capitalize()

        if Round == "Y" or Round == "N":
            break
        else:
            pass
    if Round == "Y":
        return True
    elif Round == "N":
        return False


print("")

print("Welcome to [Rock / Paper / Scissors] ")

print("")

while True:
    if Play_Again():
        Round_Count += 1
        Rock_Paper_Scissors()
    else:
        break

if Rock_Paper_Scissors():
    Player_Wins += 1
else:
    Ai_Wins += 1

print(f"{Player_Wins} / {Ai_Wins}")

print("No more Rock, Paper ,Scissors then")
