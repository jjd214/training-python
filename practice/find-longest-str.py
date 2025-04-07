# Find the longest string in a list of strings

def find_longest_word(input_str):
    words = input_str.split()
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word, len(longest_word)

input_str = input("Enter a string: ").lower()

longest_word, characters = find_longest_word(input_str)

print(f"The longest word is: {longest_word}")
print(f"The total characters is: {characters}")


# mystr = ["hello", "world", "this is a string"]

# longest_str = mystr[0]

# for i in range(len(mystr)):
#     if len(mystr[i]) > len(longest_str):
#         longest_str = mystr[i]
#     else:
#         continue

# print(f"The longest word is: {longest_str}")
# print(f"Result: {len(longest_str)}")
