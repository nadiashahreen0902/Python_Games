
#Loop
    #Ask: roll the dice?
    #If user enters Y
    #  Generate two numbers
    #  Print them
    #If user enters N
    #   Print thank you!
    #Else
    #  Print invalid choice
import random

user_times = int(input("Enter the number of times to roll the dice: "))
count = 0
for i in range(user_times):
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        count = count+1
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif(choice == 'n'):
        print("Thanks for playing:)")
        break 
    else:
        print("invalid choice!")
print("No of times the dice was rolled is:",count)