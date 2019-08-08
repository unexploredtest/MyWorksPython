# Series for a number of Fibonacci Sequance
n = int(input("How many terms would you like to compute?"))

Fib = [1,1]
print(1)
print(1)

for i in  range(2, n):
    Fib.append(Fib[i-2] + Fib[i-1])
    print(Fib[i])

# If you wanted to store the sequance:
# with open("Fibonacci.txt", "w") as write:
#     write.writelines(str(Fib))

# If you wanted to know the golden ratio:
for i in range(1,n):
    e = Fib[i] / Fib[i-1]
    print(e)
