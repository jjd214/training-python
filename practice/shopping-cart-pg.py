# Shopping cart program

isTrue = True

foods = []
prices = []

while isTrue:
    food = input("Enter a food (q to quit): ").lower()

    if food == "q":
        isTrue = False
        break

    price = float(input(f"Enter the price of {food}: "))

    foods.append(food)
    prices.append(price)

print("--- Shopping Cart ---")

for i in range(len(foods)):
    print(f"{foods[i]} - {prices[i]}")

print(f"Total: {sum(prices)}") 