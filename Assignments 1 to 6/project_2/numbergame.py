# Guess the Number game by computer
# 1 to 100 numbers.

import random
def guess_the_number():
    """Guess the number game by computer"""
    number = random.randint(1, 100)
    guesses_left = 7
    #welcome message
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    #loop generated
    while guesses_left > 0:
        print(f"\n you have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess of another number. "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        #guess the secret number
        if guess < number:
            print("Your guess is too low. Tell another!")
        elif guess > number:
            print("Your guess is too high. Tell another!")
        else:
            print(f"Good job! You guessed the number in {7 - guesses_left + 1} tries.")
            return
        guesses_left -= 1
    print(f"Sorry, you didn't guess the number. It was {number}.")

#call the function
guess_the_number()    