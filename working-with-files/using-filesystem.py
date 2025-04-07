import os
from os import path
import shutil
from zipfile import ZipFile

if path.exists("newfile.txt"):
    # Get path dir
    src = path.realpath("newfile.txt")
    # backup copy of the file concat (append) bak to the name
    dst = src + ".bak"
    # Use shell to make a copy of the file
    # This copy only the content of the file (excluding metadata)
    # shutil.copy(src, dst)

    # Rename original file 
    # os.rename("textfile.txt", "newfile.txt")
    # os.rename("txtfile.txt", "newfile.txt")

    # Put thing into ZIP Archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    #            Name of the archive 
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("textfile.txt")