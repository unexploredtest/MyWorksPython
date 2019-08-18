# Text = open("Information/genuine.txt")
#
# for line in Text:
#     print(line.rstrip())
#
# Text.seek(50)
# Text_List = Text.readlines(100)
#
# print(Text_List)

def see_line(line):
    return "Do not" in line


with open("Information/genuine.txt") as textlol:
    SEE = list(filter(see_line, textlol))
    for a in SEE:
        print(a)
