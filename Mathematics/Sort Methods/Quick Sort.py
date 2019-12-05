
def pivot_numbers(numbers):

    if len(numbers) > 1:
        pivot = numbers[(len(numbers)//2)]
        less_pivot = []
        equal_pivot = []
        more_pivot = []

        for num in numbers:
            if num > pivot:
                more_pivot.append(num)
            elif num == pivot:
                equal_pivot.append(num)
            else:
                less_pivot.append(num)

        pivoted_numbers = less_pivot+equal_pivot+more_pivot
        global less_pivot_size
        less_pivot_size = len(less_pivot)

        return pivoted_numbers

    else:
        return numbers




def quick_sort(numbers):

    if len(numbers) > 2:

        pivot = numbers[(len(numbers)//2)]
        less_pivot = []
        equal_pivot = []
        more_pivot = []

        for num in numbers:
            if num > pivot:
                more_pivot.append(num)
            elif num == pivot:
                equal_pivot.append(num)
            else:
                less_pivot.append(num)

        return quick_sort(less_pivot) + equal_pivot + quick_sort(more_pivot)

    elif len(numbers) == 2:
        if numbers[0] > numbers[1]:
            return [numbers[1], numbers[0]]

        else:
            return numbers
    else:
        return numbers


quick_sort([1, 556, 23, 6, 8, 3, 4, 6, 1, 56, 55, 222, 77, 9])
