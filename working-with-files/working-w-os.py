import os
from os import path
import time 
from datetime import datetime

#                       means get modification time of the file
#                       getctime() creation time
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# calculate how long the file was modified
                                # Big numbers of milisecs
td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(td)
print(f"Or, {td.total_seconds()} secs")
# print(os.name)

# print(f"Item exists: {path.exists("textfile.txt")}")
# print(f"Item is a file: {path.isfile("textfile.txt")}")
# print(f"Item is a directory: {path.isdir("textfile.txt")}")

# print(f"Items path: {path.realpath("textfile.txt")}")

# file_path = path.realpath("textfile.txt")

# print(f"Items path and name: {path.split(file_path)}")
