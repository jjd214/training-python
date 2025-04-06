# Rock paper scissors game
import random
import time

options = ["rock", "paper", "scissors"]

while True:
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")

    ch = random.choice(options)

    user_input = input("Enter your choice: ").lower()

    if user_input in options:
        time.sleep(1)
        print(f"The engine played {ch}")

        if ch == "rock" and user_input == "scissors":
            print("You lose")
        elif ch == "paper" and user_input == "rock":
            print("You lose")
        elif ch == "scissors" and user_input == "paper":
            print("You lose")
        elif ch == user_input:
            print("It's a tie")
        else:
            print("You win!")
    else:
        break    

    




