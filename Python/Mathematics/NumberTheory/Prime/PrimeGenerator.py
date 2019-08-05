
a = int(input("Choose a number to see its less primes:"))
p = [2,3,5]
for i in range(7, a+1):
    if i <= a:
        f = 2
        while (i % f != 0) and (f <= i**0.5):
            f += 1
        if f > i**0.5:
            print(i)
            p += [i]
    else:
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
