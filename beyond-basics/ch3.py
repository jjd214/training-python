# List comprehension


numbers = [1,2,3,4,5,6,7,8,9,10]

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(even)
print(odd)


# fruits = ["apple", "banana", "mango"]

# upper_fruits = [fruit.upper() for fruit in fruits]

# print(upper_fruits)

# start = 1
# end = 10

# doubles = [num * 2 for num in range(start, end+1)]
# triples = [num * 3 for num in range(start, end+1)]

# print(triples)