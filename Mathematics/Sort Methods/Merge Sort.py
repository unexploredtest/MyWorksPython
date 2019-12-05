import math

def devide(numbers):

    if len(numbers) > 1:
        yield numbers[:(len(numbers)//2)]
        yield numbers[(len(numbers)//2):]
    else:
        return numbers


def merge_sort(numbers):

    times = math.ceil(math.log(2, len(numbers)))

    for i in range(times):
