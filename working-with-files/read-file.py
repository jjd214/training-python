#                                  Read mode (read content)
sample_file = open("textfile.txt", "r")

if sample_file.mode == "r":
    # contents = sample_file.read()
    file_lines = sample_file.readlines()
    for file_line in file_lines:
        print(file_line)