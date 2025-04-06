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




# # For Loops

# for i in range(1, 21):
#     if i == 13:
#         continue
#     print(i)
        

# for i in reversed(range(1, 11, 2)):
#     print(i)

# print("Happy new year everyone!")




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


