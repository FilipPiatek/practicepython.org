# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num = random.randint(1, 9)

quit = ""
while quit != "exit":
    guess = int(
        input(
            "I'm thinking of a number between 1 and 9. What number am I thinking of?? "
        ))
    if guess == num:
        print("Congratulations!! You guessed it!")
        quit = input("Type 'exit' to quit ")
    elif guess > num:
        print("My number is lesser than yours")
        quit = input("Type 'exit' to quit or press ENTER to try again")
    else:
        print("My number is greater than yours")
        quit = input("Type 'exit' to quit or press ENTER to try again")
