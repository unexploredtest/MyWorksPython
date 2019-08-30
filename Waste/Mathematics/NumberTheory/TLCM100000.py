from Prime.Prime import list
from Simple.TLCM import TLCM

tlcm = 1

for i in list:
    tlcm = tlcm * i
    print(i)
non_prime = [i for i in range(1,100001) if i not in list]
print(non_prime)
non_prime.append(tlcm)
y = TLCM(non_prime)

with open("num.txt", "w") as num:
    num.write(str(y))
print("Done")

print(len(str(y)))
