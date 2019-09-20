
def insert(numbers, right_index, value):

    for i in range(right_index, -1, -1):
        if value >= numbers[i]:
            numbers = numbers[:i+1] + [value] + numbers[i+1:right_index+1] + numbers[right_index+2:]
            break
    else:
        numbers = [value] + numbers[:right_index+1] + numbers[right_index+2:]

    return numbers


def insertion_sort(numbers):

    i = 0
    for num in numbers[1:]:
        numbers = insert(numbers, i, num)
        i += 1

    return numbers


nums = [1, 556, 23, 6, 8, 3, 4, 6, 1, 56, 55, 222, 77, 9]
print(insertion_sort(nums))
