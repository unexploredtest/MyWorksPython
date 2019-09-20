# Some important functions

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
            # print(g)
        c = g
    return int(c)


if __name__ == "__main__":
    a = TLCM(list_past(100))
    print(a)
