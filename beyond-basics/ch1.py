# # Consession stand program

# menu = {
#     "pizza": 100,
#     "fries": 80,
#     "hamburger": 50,
#     "tacos": 120,
#     "sisig": 70
# }

# cart = []
# total = 0

# print("---------- MENU ----------")

# for key, value in menu.items():
#     print(f"{key.capitalize():10} - {value:.2f}")

# print("--------------------------")

# while True:
#     food = input("Enter your order (q to quit): ").lower()

#     if food == "q":
#         break

#     if food in menu:
#         cart.append(food)
#         total += menu.get(food)

#     else:
#         print("Invalid order")     

# print("---------- CART ----------")
# for item in cart:
#     print(f"{item.capitalize():10} - {menu[item]:.2f}")
# print("--------------------------")
# print(f"Total: {total:.2f}")











# Dictionary


# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# fruits.pop(1) 
# print(fruits)

# capitals = {
#     "USA": "Washington, D.C.",
#     "Philippines": "Manila",
#     "Japan": "Tokyo",
#     "South Korea": "Seoul",
#     "China": "Beijing",
# }

# capitals.update({"India": "New Delhi"})
# capitals.update({"USA": "Chicago, D.C."})
# capitals.pop("India")
# capitals.popitem()

# for key, value in capitals.items():
#     print(f"{key}: {value}")

# for val in capitals.values():
#     print(val)

# print(capitals)




# if capitals.get("USA"):
#     print("That capital exists in dictionary")
# else:
#     print("That capital does not exist in dictionary")

# # Quiz game

# questions = (
#     "What is the capital of France?",
#     "What is the largest planet in our solar system?",
#     "What is the chemical symbol for gold?",
#     "What is the largest mammal in the world?",
#     "What is the smallest country in the world?",
# )

# options = (
#     ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
#     ("A. Jupiter", "B. Saturn", "C. Mars", "D. Earth"),
#     ("A. Au", "B. Ag", "C. Pb", "D. Fe"),
#     ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Hippopotamus"),
#     ("A. Vatican City", "B. Monaco", "C. Nauru", "D. San Marino"),
# )

# answers = ("A", "A", "A", "A", "A")

# guess = []

# for i in range(len(questions)):
#     print(questions[i])
#     for j in range(len(options[i])):
#         print(options[i][j], end=" ")
#     print()
#     temp_guess = input("Enter your answer (A, B, C, D): ").upper()
#     guess.append(temp_guess)

# show_score = []

# count = 1

# for i in range(len(answers)):
#     if guess[i] == answers[i]:
#         show_score.append(f"{count}. correct!")
#     else:
#         show_score.append(f"{count}. incorrect!")
#     count += 1


# print("--- Score ---")
# for i in show_score:
#     print(i)



# # fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # vegetables = ["carrot", "broccoli", "spinach", "potato", "tomato"]
# # dairy = ["milk", "cheese", "yogurt", "butter", "cream"]

# calcu = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     ["*", 0, "="] 
# ]

# for row in calcu:
#     for col in row:
#         print(col, end=" ")
#     print()


# groceries = [
#     ['appel', 'banana', 'cherry'],
#     ['carrot', 'broccoli', 'spinach'],
#     ['milk', 'cheese', 'yogurt']
# ]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()
# # Shopping cart program

# isTrue = True

# foods = []
# prices = []

# while isTrue:
#     food = input("Enter a food (q to quit): ").lower()

#     if food == "q":
#         isTrue = False
#         break

#     price = float(input(f"Enter the price of {food}: "))

#     foods.append(food)
#     prices.append(price)

# print("--- Shopping Cart ---")

# for i in range(len(foods)):
#     print(f"{foods[i]} - {prices[i]}")

# print(f"Total: {sum(prices)}")   


# which = input("Enter which number to count (even / odd): ")



# numbers = [2, 5, 20, 30, 55]

# def counter(which, numbers):
#     count = 0
#     if which == "even":
#         for number in numbers:
#             if number % 2 == 0:
#                 count += 1
#     elif which == "odd":
#         for number in numbers:
#             if number % 2 != 0:
#                 count += 1
#     else:
#         print("Invalid input")
#         return None
    
#     return count

# res = counter(which, numbers)
# print(f"Input: {which}, {numbers}")
# print(f"Result: {res}")
# # Collections


# fruits = {"apple", "banana", "cherry", "orange", "kiwi", "mango","pear"}

# # fruits.append("kiwi") # add "kiwi" to the end of the list
# # fruits.remove("kiwi") # remove "kiwi" from the list
# # fruits.insert(2, "pineapple") # insert "pineapple" at index 2
# # fruits.sort() # sort the list in ascending order
# # fruits.reverse() # reverse the list
# # fruits.clear() # clear the list
# # fruits.insert(fruits.index("kiwi"), "kiwi") 
# # print(fruits.count("kiwi")) # count the number of occurences of "kiwi" in the list
# print(fruits)
# # print("kiwi" in fruits) # check if "kiwi" is in the list
# # for i in range(len(fruits)):
# #     print(fruits[i])



# # Countdown timer program
# import time

# my_time = int(input("Enter the time in seconds: "))

# for i in reversed(range(1, my_time + 1)):
#     seconds = i % 60
#     minutes = int(i / 60) % 60
#     hours = int(i / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1) 

# print("Time's up!")
# # For Loops

# for i in range(1, 21):
#     if i == 13:
#         continue
#     print(i)
        

# for i in reversed(range(1, 11, 2)):
#     print(i)

# print("Happy new year everyone!")




# # Challenge 1: Compound interest calculator

# principle = 0
# rate = 0
# time = 0

# isTrue = True

# while principle == 0:
#     principle = float(input("Enter the principle amount: "))

#     if principle <= 0:
#         print("Principle amount must be greater than 0")
#         principle = 0

# while rate == 0:
#     rate = float(input("Enter the rate of interest: "))

#     if rate <= 0:
#         print("Rate of interest must be greater than 0")
#         rate = 0

# while time == 0:
#     time = float(input("Enter the time in years: "))

#     if time <= 0:
#         print("Time must be greater than 0")
#         time = 0

# total = principle * (1 + rate / 100) ** time
# interest = total - principle

# print(f"Total amount after {time:.0f} years is: {total:.2f}")
# print(f"Interest earned is: {interest:.2f}")





# isTrue = True
# while isTrue:
#     food = input("Enter your favourite food (q to quit): ")

#     if food == "q":
#         print("You have quit the program")
#         break

#     print(f"Your favourite food is {food}")






# # format specifier: python

# price1 = 13.1416
# price2 = 245.582
# price3 = 5.62234

# print(f"Price 1: {price1:10}")
# print(f"Price 2: {price2:10}")
# print(f"Price 3: {price3:10}")





# # Indexing

# credit_number = "1234-5678-9012-3456x"
# print(credit_number[0]) # prints the first character of the string

# 13-68
# print(credit_number[:5])







# # Validate user input exercise

# isTrue = True

# while isTrue:
#     username = input("Enter your username: ")
#     if len(username) > 12:
#         print("Username must be less than 12 characters")
#         continue

#     elif username.find(" ") != -1:
#         print("Username must not contain spaces")
#         continue

#     elif username.isalpha() == False:
#         print("Username must be alphanumeric")
#         continue
    
#     else:
#         print("Username is valid")
#         break







# # String methods    

# name = input("Enter your name: ")

# # result = name.find(" ") # get the index of the first occurence in the string
# # result = name.find(" ", 0, 5) # get the index of the first occurence in the string from index 0 to 5
# # result = name.rfind(" ") # get the index of the last occurence in the string

# # name = name.capitalize() # capitalize the first letter of the string
# # name = name.title() # capitalize the first letter of each word in the string
# # name = name.upper() # convert the string to uppercase
# # name = name.lower() # convert the string to lowercase
# # name = name.isdigit() # check if the string is a digit
# # name = name.isalpha() # check if the string is alphabetic
# # name = name.isalnum() # check if the string is alphanumeric


# phone_number = "0960-565-6273"

# res = phone_number.count("-") # count the number of occurences of "-" in the string
# res = phone_number.replace("-", "/") # replace "-" with "" in the string

# print(res)

# print(f"length of name is {len(name)}")





# # List []
# mylist = [1, 2, 3, 4, 5]

# print(f"The length of the list is: {len(mylist)}")







# # Variables
# myint = 5
# myfloat = 5.0
# mystr = "Jacob"
# mybool = True

# # Logical Operators & Comparison Operators
# print(mystr == "Jacob" and myint == myfloat)
# print(mystr == "jacob" or myint <= myfloat)
# print(mystr != "Jacob" or not(myint != myfloat))


