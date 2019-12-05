# importing the module
import os

# getting all of the available methods and attributes within a module
print(dir(os))

# getting the current directory
print(os.getcwd())

# changing the directory
os.chdir("C:/Users/aliPMPAINT/Documents/GitHub/MyWorksPython/Practice/OS Mudole/test")

# getting list of all the files and foolder
print(os.listdir())

# making just one directory
os.mkdir("loltest")

# making one or more directory
os.makedirs("players/noob")

# removing just one directory
os.rmdir("loltest")

# removing one or more directory
os.removedirs("players/noob")

# renaming a file or folder
os.rename("idk.txt", "idk.txt")

# information about a file or folder
print(os.stat("idk.txt"))

# if you wanted to know the size of a file(in bits)
print(os.stat("idk.txt").st_size)
