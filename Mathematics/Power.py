
def power(number, raiser):

    if raiser > 0:

        if raiser % 2 != 0:
            return number * power(number, raiser-1)
        else:
            return power(number, raiser/2) * power(number, raiser/2)

    elif raiser == 0:
        return 1

    else:
        return 1 / power(number, -1 * raiser)


print(power(2, -5))
