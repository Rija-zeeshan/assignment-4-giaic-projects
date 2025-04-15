# Guess the Number Game Python Project (user)

import random
print("Welcome to Guess the Number Game")
print("You have to guess the number between 1 to 100")
#generate random number 
number = random.randint(1, 100)
while True:
    guess = int(input("Enter your guess number: "))
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Congratulations! You guessed the number")
        break
        