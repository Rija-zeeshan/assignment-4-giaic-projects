# Rock, Paper, Scissors Game

import random

print("Welcome to Rock, Paper, Scissors Game")
# game choices
choices = ["rock", "paper", "scissors"]
# user choice
player_choice = input("Enter your choice: rock, paper, or scissors: ").lower()

# computer choice
computer_choice = random.choice(choices)

#winner decission
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"players wins! {player_choice} beats {computer_choice}")
elif player_choice == "paper" and computer_choice == "rock":
    print(f"players wins! {player_choice} beats {computer_choice}")
elif player_choice == "scissors" and computer_choice == "paper":
    print("players wins! {player_choice} beats {computer_choice}")
else:
    print(f"Computer wins! {computer_choice} beats {player_choice}")