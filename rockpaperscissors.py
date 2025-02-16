#Ask the user to make a choice
#If choice is invalid
#   Print an error
#Let the computer make a choice
#Print choices(emojis)
#Determine the winner
#Ask user if he wants to continue or not
#If not 
# Simply terminate
import random

emojis = {'r':'🪨','p':'📃','s': '✂️'}
choices = ('r','p','s')#converting to tuple as they become read only
def get_user_choice():
    while(True):
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")
def display_choices(user_choice,computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print('You win')
    else:
        print('You Lose')
def play_game():   
    while(True):
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)
        should_continue = input("Continue(y/n): ").lower()
        if should_continue == 'n':
            break
play_game()