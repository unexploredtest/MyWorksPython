from Primes2s1000000 import *

a1 = [i for i in range(100,1000) if i in a]
a_s = [i**2 for i in a1]

a2 = [i for i in range(32,100) if i in a]
a_c = [i**3 for i in a2]


a3 = [i for i in range(15,32) if i in a]
a_4 = [i**4 for i in a3]

a4 = [i for i in range(10,15) if i in a]
a_5 = [i**5 for i in a4]

a_else= [2**19, 3**12, 5**8, 7**7]

a_big = [i for i in a if i > 1000]

a_finally = sorted((a_s + a_c + a_4 + a_5 + a_else + a_big))

with open("file_tlcm.txt", "w") as text:
    text.writelines(str(a_finally))
