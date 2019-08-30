# A is the first input and B is the second input and n is the digit.

A = input()
B = input()
n = int(input())

# We first make a list and put the first two elements

listAB = [A, B]

#

i = 2

while len(listAB[i - 1]) < n:
    listAB.append((listAB[i-2]+listAB[i-1]))
    i += 1

wanted_number = listAB[i-1]

print(wanted_number[n-1])
print(listAB)
