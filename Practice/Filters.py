Grades = [15, 19, 20 , 20, 17.75, 18.25, 20, 20, 19.5, 19.25]

# filter method

def I_G(Grade):
    return Grade < 19
Fixed_G = list(filter(I_G, Grades))
print(Fixed_G)

# loop method

New_G = [ ]
for G in Grades:
    if G < 19:
        New_G.append(G)
print(New_G)

# list comprehension method

Lol_G = [G for G in Grades if G < 19]
print(Lol_G)
