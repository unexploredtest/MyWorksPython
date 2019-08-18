def lol(number = 100):
    n = number*100+89
    return n

nums = [5,8,6,3,6,8,4,3,5,8,11,68,3,257]

# Using maps

lolnums = list(map(lol, nums))
print(lolnums)

# Using List Comprehension

lolnums = [lol(k) for k in nums]
print(lolnums)
