# List Comprihension vs For Looo

num = [
1,2,3,4,5,6,7,
11,12,13,14,15
]

print(num)

# Triple value by to methods:

# The first method(For Loop):

num31 = [ ]
for n in num:
    num31.append(n*3)
print(num31)

# The secound method(List Comprihension):

num32 = [n*3 for n in num]
print(num32)

# I want to squre the even numbers by two methods:

# The first method(For Loop):

num21 = [ ]
for n in num:
    if n % 2 == 0:
        num21.append(n**2)
print(num21)

# The secound method(List Comprihension):

num22 = [n**2 for n in num if n % 2 == 0]
print(num22)
