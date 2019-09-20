# Here, we'll create a binary search for a list:


def binary_search(list, number):

    min, max = 0, len(list) - 1
    guess = max // 2

    while list[guess] != number and max >= min:

        if list[guess] > number:
            max = guess - 1
            guess = (max+min) // 2
        elif list[guess] < number:
            min = guess + 1
            guess = (max+min) // 2

    if list[guess] == number:
        print(f"Found at index {guess}!")
        return guess
    else:
        print("Doesn't exist!")
        return False


binary_search([1, 3, 5, 8, 10, 14, 17, 75, 82, 95, 101, 107, 108, 110], 8)
binary_search([1, 3, 5, 8, 10, 14, 17, 75, 82, 95, 101, 107, 108, 110], 92)
