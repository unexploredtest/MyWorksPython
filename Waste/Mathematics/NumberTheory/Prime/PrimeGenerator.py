from Primes1000000 import *

primes = a

n = int(input("Choose a number to see its less primes:"))
p = [2,3,5]

if n < 1000000:

    p = [i for i in primes if i < n]

elif n < 99999660000289:

    p = primes

    for i in range(1000001, n+1, 2):

        f = 0

        while (i % p[f] != 0) and (p[f] <= i**0.5):
            f += 1

        if p[f] > i**0.5:
            print(i)
            p += [i]

else:

    for i in range(7, n+1):
        if i <= n:
            f = 2
            while (i % f != 0) and (f <= i**0.5):
                f += 1
            if f > i**0.5:
                print(i)
                p += [i]

print("DONE!")
print(f"The number of prime is {len(p)}")
print(p)
b = input("Do you want to save the prime numbers into the list? (y/n)")
if b == "y":
    with open("Primes.txt", "w") as Primes:
        Primes.write(str(p))
    print("It is saved as (Primes.txt), Goodbye.")
else:
    print("Goodbye.")
