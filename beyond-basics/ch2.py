
# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")

#     print()
#     print(f"{kwargs.get("country")}")
#     print(f"{kwargs.get("city")}, {kwargs.get("apartment")}")

# shipping_label("Sr.","John Jacob", "Dimaya",
#                country="Philippines",
#                city="Makati",
#                apartment="521")



# def numbers(*args):
#     for arg in args:
#         print(arg)

# numbers(1,2,3,4,5)


# def greetings(greet, fname, lname):
#     print(f"{greet}, Mr. {fname} {lname}")

# greetings(greet="Good day!", lname="Dimaya", fname="Jacob")

# print("1","2","3", sep="-")

# import time

# def countdown(end,start=0):
#     for sec in range(start, end+1):
#         print(sec)
#         time.sleep(1)

# countdown(10)



# # Find the longest string in a list of strings

# mystr = ["hello", "world", "this is a string"]

# longest_str = mystr[0]

# for i in range(len(mystr)):
#     if len(mystr[i]) > len(longest_str):
#         longest_str = mystr[i]
#     else:
#         continue

# print(f"The longest word is: {longest_str}")
# print(f"Result: {len(longest_str)}")



# # Rock paper scissors game
# import random
# import time

# options = ["rock", "paper", "scissors"]

# while True:
#     print("Welcome to Rock, Paper, Scissors!")
#     print("Type 'rock', 'paper', or 'scissors' to play.")
#     print("Type 'exit' to quit the game.")

#     ch = random.choice(options)

#     user_input = input("Enter your choice: ").lower()

#     if user_input in options:
#         time.sleep(1)
#         print(f"The engine played {ch}")

#         if ch == "rock" and user_input == "scissors":
#             print("You lose")
#         elif ch == "paper" and user_input == "rock":
#             print("You lose")
#         elif ch == "scissors" and user_input == "paper":
#             print("You lose")
#         elif ch == user_input:
#             print("It's a tie")
#         else:
#             print("You win!")
#     else:
#         break    

    






# # Number guessing game

# import random

# magic_number = random.randint(1, 100)
# attempts = 0

# while True:
#     guess = int(input("Guess the magic number (1-100):"))

#     if guess == magic_number:
#         print("You guessed it!")
#         print(f"You took {attempts} attempts.")
#         break
#     elif guess < magic_number:
#         print("Too low!")
#     else:
#         print("Too high!")
#     attempts += 1


# import random

# options = ["rock", "paper", "scissors"]
# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# random.shuffle(cards)
# ch = random.choice(options)

# print(ch)