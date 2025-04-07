def string_palindrome(str):
    clean_str1 = str.replace(" ", "")
    reversed_text = "".join(reversed(clean_str1))

    return clean_str1 == reversed_text

input_str = input("Enter a string: ").lower()

res = string_palindrome(input_str)

print(f"result: {res}")