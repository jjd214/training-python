# Find the longest string in a list of strings

mystr = ["hello", "world", "this is a string"]

longest_str = mystr[0]

for i in range(len(mystr)):
    if len(mystr[i]) > len(longest_str):
        longest_str = mystr[i]
    else:
        continue

print(f"The longest word is: {longest_str}")
print(f"Result: {len(longest_str)}")
