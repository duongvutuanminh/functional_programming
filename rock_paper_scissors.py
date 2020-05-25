#creating a Rock,Paper, Scissors game(project 2)
import random
import time

tool_list = ["Rock","Paper","Scissors"]
pc = random.choice(tool_list)
print("Welcome to the game! \nPlease choose Rock, Paper or Scissor!\n  1.Rock\n  2.Paper\n  3.Scissors")
player = input()


for item in list(range(1,4)):
    print(item)
    time.sleep(1)

playing_rules = {"1":"Rock", "2":"Paper","3":"Scissors" }
print(f"You choose: {playing_rules[player]}")    
print(f"The computer choose: {pc}")

if player == "1":
    if pc == "Paper":
        print("Player Lose!")
    elif pc == "Rock":
        print("Draw!")
    else:
        print("Player win!")
elif player == "2":
    if pc == "Scissors":
        print("Player Lose!")
    elif pc == "Paper":
        print("Draw!")
    else:
        print("Player win!")
else:
    if pc == "Rock":
        print("Player Lose!")
    elif pc == "Scissors":
        print("Draw!")
    else:
        print("Player win!")

