from random import *
def cpu_choice():
    options = ["Rock","Paper","Scissors","Lizard","Spock"]
    cpu = choice(options)
    return cpu

def player_choice():
    player_choice = input("Choose between Rock, Paper, Scissors, Lizard, or Spock:")
    print(player_choice.upper)
    while player_choice.upper() not in ["ROCK","PAPER","SCISSORS","LIZARD","SPOCK"]:
        player_choice = input("That's not an option, choose between Rock, Paper, Scissors, Lizard or Spock:")
    return player_choice
def results(cpu,player):
 result = ""

 cpu = str(cpu).upper()
 player = str(player).upper()
 player_wins = False
 if player in ["SCISSORS","LIZARD"] and cpu == "ROCK":
     player_wins = True
 if player in ["ROCK","SPOCK"] and cpu == "PAPER":
     player_wins = True
 if player in ["ROCK","SPOCK"] and cpu == "SCISSORS":
     player_wins = True
 if player in ["PAPER","SPOCK"] and cpu == "LIZARD":
     player_wins = True
 if player in ["PAPER","LIZARD"] and cpu == "SPOCK":
    player_wins = True
 if player == cpu: 
    return "Draw"
 elif player_wins == True:
    return "Win"
 else: return "Lose"
 
player = player_choice()
cpu = cpu_choice()
print("Player Choice:",player)
print("CPU Choice:",cpu)
result = results(cpu,player)
print(result)

if result == "Draw": print("It's a draw")
elif result == "Win": print(player, "beats", cpu,"You win!")
elif result == "Lose": print(cpu,"beats",player,"You lose!")
else: print("Nothing returned")
     

 



       