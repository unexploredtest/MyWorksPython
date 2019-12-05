
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


pivot_numbers([4,7,1,7,8,3,4])


def quick_sort(numbers):

    if len(numbers) > 2:

        pivoted_numbers = pivot_numbers(numbers)
        return quick_sort(pivoted_numbers[:less_pivot_size]) + [pivoted_numbers[less_pivot_size]] + quick_sort(pivoted_numbers[less_pivot_size+1:])

    else:
        return pivot_numbers(numbers)

quick_sort([4,7,1,7,8,3,4])
