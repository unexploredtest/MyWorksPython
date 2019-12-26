import random

# produce a random value in interval [0,1)
value = random.random()
print(value)

# get a random floating number between two numbers
value = random.uniform(1 ,10)
print(value)

# get a random integer between two numbers (including both numbers)
value = random.randint(1, 6)
print(value)

# get a random thing from a set
names = ["Ali", "Mohammad", "Mehdi", "Corey", "Jack"]
value = random.choice(names)
print(value)

# get multiple random choices from a list
colors = ["red", "green", "blue"]
value = random.choices(colors, k=10)
print(value)

# get multiple random choices from a list with given probability of showing up
colors = ["red", "green", "blue"]
value = random.choices(colors, k=10, weights=[3,15,2])
print(value)

# change the order of a list(shuffle it)
numbers = list(range(1, 21))
random.shuffle(numbers)
print(numbers)

# choose random list things but unique(no repeated choice)
numbers = list(range(1, 21))
value = random.sample(numbers, k=5)
print(value)
