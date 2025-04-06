#                                   Means create a file if it does'nt exist.
# sample_file = open("textfile.txt", "w+")

# sample_file.write("This is sample text")

# sample_file.close()
#                                   Means append a text to the end (not overwrite)
sample_file = open("textfile.txt", "a+")

sample_file.write("This is a text to append at the end.")
sample_file.write("This is a also a text to append at the end.")

sample_file.close()