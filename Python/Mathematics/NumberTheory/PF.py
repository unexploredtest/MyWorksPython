import numpy as np
num = np.arange(0, 100, 1)
nums = [n**2+n+41 for n in num]

import time
r = "If you want to try another integer, press Enter"
r += ", if finished, press any other key:"
for a in nums:
    # a = int(input("Choose an integer to see if it is prime or composite:"))
    i = 2
    time1 = time.process_time()
    if a > 1:
        while a % i != 0:
            i += 1
    time2 = time.process_time()
    if i < a:
        print(f"{a} is composite and its smallest factor is {i}.")
    elif i == a:
        print(f"{a} is prime.")
    else:
        print("1 is neither prime nor composite.")
    time3 = time2 - time1
    # print(f"The time token to do the calculations is {time3} secounds.")
    # z = input(f"{r}")
    # if z == "":
    #     continue
    # else:
    #     break
