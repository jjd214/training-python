
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







# import random

# options = ["rock", "paper", "scissors"]
# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# random.shuffle(cards)
# ch = random.choice(options)

# print(ch)