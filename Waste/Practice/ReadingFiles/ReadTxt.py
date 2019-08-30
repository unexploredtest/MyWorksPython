# How to read a file
Login_Info = open("Information/log.txt")

# If you would like to read all lines with a gap:
for line in Login_Info:
    print(line)

# If you wanted to reset or read the text from a particular word:
Login_Info.seek(50)

# If you would like to not have a space bitween lines:
for line in Login_Info:
    print(line.rstrip())

Login_Info.seek(0)

# To make a list with lines as string elements:
List_Lines = Login_Info.readlines()
print(List_Lines)

# Happen we need to sart from a particulary letter,
# and just need to read to a specific number of letters, you do this:

Login_Info.seek(110)
PLogin_Info = Login_Info.read(200)
print(PLogin_Info)

# If we wanted to close the file:

Login_Info.close()

# If you wanted to just use it to not forget to close it (solution in line 38)
# If you wanted to how just the lines which have a paricular words or lines:

def See(line):
    return "HTTP" in line

with open("Information/log.txt") as log:
    a = list(filter(See, log))
    print(a)
