# File Detection :
# this shows that weather it is file or folder and does it exist or not
import os

path = "/Users/darshandhanwade/Desktop/file"

if os.path.exists(path):
    print("that location exists ")

    if os.path.isfile(path):
        print("this is a file")

    elif os.path.isdir(path):
        print("this is a folder ")


else:
    print("that location dosen't exists ")


# COPY FILE :
# copyfile() = copies content of a file
# copy() = copyfie() + premission mode + destination can be directory
# copy2() = cpoy() + cpoies metadata (file's creation and modification time)
    
import shutil

shutil.copyfile('Python Intermediate/file.txt','copy.txt') # source and destination argument needed

# copy2() and copy() both need same arguments  


# MOVE FILE:

import os

source = "/Users/darshandhanwade/Public/Code Here/Python/Python Intermediate/folder"
destinstion = "/Users/darshandhanwade/Library/Mobile Documents/com~apple~CloudDocs/deskstop"

try:
    if os.path.exists(destinstion):
        print("there is alredy file ")
    else:
        os.replace(source,destinstion)
        print(source + " was moved")


except FileNotFoundError:
    print(source + " was not found ") 

# DELETE FILE 
import os
path = "/Users/darshandhanwade/Public/Code Here/Python/Python Intermediate/emptyfile.txt"

try:
    os.remove(path)

except FileNotFoundError:
    print("that file was not found ")


