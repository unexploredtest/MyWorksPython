# Some important functions
from Primes100000 import *
# Returns a list for a number and its n-1, n-2, ..., 2, 1
def list_past(number):
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    return numbers

# Detirmines The Least Common Multipul(TLCM) for two or more numbers
def TLCM(list_numbers):
    list_numbers = sorted(list_numbers)
    list_numbers.reverse()
    c = list_numbers[0]
    g = c
    for i in list_numbers:
        print(i)
        c = g
        while g % i != 0:
            g += c
            #print(g)
        c = g
    return int(c)

def TLCM2(list_numbers):
    if max(list_numbers) < 100000:
        from Primes100000 import get_prime
    else:
        from Primes1000000 import get_prime

    allprimes = get_prime(max(list_numbers))
    someprimes = [i for i in allprimes if i in list_numbers]

    x = 1
    for n in someprimes:
        x *= n

    non_primes = [i for i in list_numbers if i not in someprimes]
    non_primes.append(x)

    return TLCM(non_primes)



if __name__ == "__main__":
    print(TLCM2(list_past(8000)), "The second value")
