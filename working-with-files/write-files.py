# .csv
import csv

employees = [
    ["name", "age", "job"],
    ["SpongeBob", 20, "cook"],
    ["Patrick", 21, "unemployed"],
    ["Sandy", 31, "Scientist"]
]

file_path = "C:/Users/Administrator/Downloads/testcsv.csv"

try:
    with open(file_path, "x", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file was created {file_path} was created")

except FileExistsError:
    print("file already exists.")


# # .json

# import json

# students = {
#     "name": "Dimaya",
#     "age": 21,
#     "course": "BSIT"
# }

# file_path = "C:/Users/Administrator/Downloads/testjson.json"

# try:
#     with open(file_path, "x") as file:
#         json.dump(students, file, indent=4)
#         print(f"json file {file_path} was created")
# except FileExistsError:
#     print("The file already exist.")








# # .txt

# text_data = "Hello world!"
# file_path = "C:/Users/Administrator/Downloads/testfile.txt"

# students = ["Dimaya", "Jancis", "Ana Bien", "Johna Grace"]

# try:
#     # same to instance obj
#     with open(file_path, "x") as file:
#         for student in students:
#             file.write(student)
#         file.write("\n" + text_data)
#         print(f"text file {file_path} was created")
# except FileExistsError:
#     print("That file already exist")


#                                   Means create a file if it does'nt exist.
# sample_file = open("textfile.txt", "w+")

# sample_file.write("This is sample text")

# sample_file.close()
#                                   Means append a text to the end (not overwrite)
# sample_file = open("textfile.txt", "a+")

# sample_file.write("This is a text to append at the end.")
# sample_file.write("This is a also a text to append at the end.")

# sample_file.close()



