nums = [4, 6, 1, 6, 7, 4, 2, 1, 744, 54, 57]

# First method

def square(num):
    return num**2

print(list(map(square, nums)))

print(list(map(lambda n: n**2, nums)))
