
def swap(list, first_index, second_index):

    first, second = list[first_index], list[second_index]
    list[first_index] = second
    list[second_index] = first


def index_of_minimum(list, start_index):

    min_num = list[start_index]
    min_index = start_index

    i = start_index

    for num in list[start_index:]:
        if num < min_num:
            min_num = num
            min_index = i
        i += 1

    return min_index


def selection_sort(num_list):

    for start in range(len(num_list)-1):

        min_index = index_of_minimum(num_list, start)
        swap(num_list, start, min_index)

    return num_list


nums = [1, 556, 23, 6, 8, 3, 4, 6, 1, 56, 55, 222, 77, 9]
print(selection_sort(nums))
