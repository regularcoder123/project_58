import random
import colorama
from colorama import Fore

def player_choice():
    user_choice = input("What is your move?:")
    return user_choice
def computer_choice():
    choices = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choices)
    return computer_choice


while True:
    print("Welcome to Rock Paper Scissors! Input 'Rock', 'Paper' or 'Scissors'")
    user = player_choice()
    computer = computer_choice()
    if user.lower() == 'rock' and computer == 'Scissors':
        print("You Chose Rock, Computer chose Scissors, You win!")

    if user.lower() == 'paper' and computer == 'Rock':
        print("You Chose Paper, Computer chose Rock, You win!")

    if user.lower() == 'scissors' and computer == 'Paper':
        print("You Chose Scissors, Computer chose Paper, You win!")
    
    if user.lower() == 'scissors' and computer == 'Rock':
        print("You Chose Scissors, Computer chose Rock, You Lose :(")
    
    if user.lower() == 'rock' and computer == 'Paper':
        print("You Chose Rock, Computer chose Paper, You Lose :(")
    
    if user.lower() == 'Paper' and computer == 'Scissors':
        print("You Chose Paper, Computer chose Scissors, You Lose :(")
    
    if user.lower() == 'rock' and computer == 'Rock':
        print("You Chose Rock, Computer chose Rock, Its a tie!")
    
    if user.lower() == 'paper' and computer == 'Paper':
        print("You Chose Paper, Computer chose Paper, Its a tie!")
    
    if user.lower() == 'scissors' and computer == 'Scissors':
        print("You Chose Scissors, Computer chose Scissors, Its a tie!")
    
    retry = input("Do you want to play again? (y/n):")
    if retry == 'n':
        break
    else:
        continue
    
    
        





