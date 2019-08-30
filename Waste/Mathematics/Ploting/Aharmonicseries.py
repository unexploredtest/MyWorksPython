# a = 1 - 1/2 + 1/3 - 1/4 + ...
sum = 0
for i in range(1, 1001000):
    print(i)
    sum += 1/i * (-1)**(i+1)
    print(sum)
