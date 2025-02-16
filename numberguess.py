#loop 
    # generate a random number(for the user to guess)
    #ask user to guess the number
    #if number > guess
    #   print too high!
    #if number < guess 
    #   print too low!
    #Else
    #   print Well done that's right
import random

number_to_guess = random.randint(1,100)
while(True):
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))
        if user_guess > number_to_guess:
            print("Too high!")
        elif(user_guess < number_to_guess):
            print("Too low!")
        else:
            print("Congratulations! You have guessed the number.")
            break
    except ValueError:#because if user enters any invalid user_guess is invalid
        print("Please enter a valid answer")  
