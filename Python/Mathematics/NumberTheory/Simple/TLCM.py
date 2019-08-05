# Some important functions

# Returns a list for a number and its n-1, n-2, ..., 2, 1
def list_past(number):
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    return numbers

# Detirmines The Least Common Multipul(TLCM) for 1 to a number
def TLCM(number):
    all_numbers = list_past(number)
    c = number
    g = c
    for i in all_numbers:
        c = g
        while g % i != 0:
            g += c
            print(g)
        c = g
    return int(c)

TLCM(5000)
