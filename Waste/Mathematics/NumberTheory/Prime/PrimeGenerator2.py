
a = 10000 # int(input("Choose a number to see its less primes:"))
p = [2]
for i in range(3, a+1, 2):
    if i <= a:
        f = 2
        while i % f != 0:
            f += 1
        if f == i:
            print(f)
            p += [f]
    else:
        print("DONE!")
print(f"The number of prime is {len(p)}")
print(p)
# b = input("Do you want to save the prime numbers into the list? (y/n)")
# if b == "y":
#     with open("Primes.txt", "w") as Primes:
#         Primes.write(str(p))
#     print("It is saved as (Primes.txt), Goodbye.")
# else:
#     print("Goodbye.")
