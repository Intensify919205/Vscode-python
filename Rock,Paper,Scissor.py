
import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player,computer):
  print(f'You Chose {player}, and computer chose {computer}')
  if player == computer:
    print("Its a tie")
  elif player == "rock":
    if computer == "scissors":
      return "Rock Smashes Scissors! You win"
      
    else:
      return "Paper covers Rock! You lose"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers Rock! You win"
    else:
      return "Scissors cuts Paper! You lose"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts Paper! You win"
    else:
      return  "Rock Smashes Scissors! You lose "
    

choices = get_choices()
result  = check_win(choices["player"], choices["computer"])
print(result)







    