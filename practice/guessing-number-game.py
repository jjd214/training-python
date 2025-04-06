# Number guessing game

import random

magic_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the magic number (1-100):"))

    if guess == magic_number:
        print("You guessed it!")
        print(f"You took {attempts} attempts.")
        break
    elif guess < magic_number:
        print("Too low!")
    else:
        print("Too high!")
    attempts += 1