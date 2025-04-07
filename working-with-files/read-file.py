import csv

file_path = "C:/Users/Administrator/Downloads/input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[1])

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission not found.")


# import json

# file_path = "C:/Users/Administrator/Downloads/input.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content.get("course"))
# except FileNotFoundError:
#     print("File does not exist.")
# except PermissionError:
#     print("You do not have permission.")




# file_path = "C:/Users/Administrator/Downloads/input.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File does not exist.")
# except PermissionError:
#     print("You do not have permission")








# #                                  Read mode (read content)
# sample_file = open("textfile.txt", "r")

# if sample_file.mode == "r":
#     # contents = sample_file.read()
#     file_lines = sample_file.readlines()
#     for file_line in file_lines:
#         print(file_line)