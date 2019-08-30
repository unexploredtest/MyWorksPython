n = int(input())
factors = [1]
i = 2
while i <= n:
    if n % i == 0:
        factors.append(i)
    i += 1
Sfactors =  [f"{n}" for n in factors]
sumfactors = []
for n in Sfactors:
    z = 0
    sum = 0
    while len(n) > z:
        sum += int(n[z])
        z += 1
    sumfactors.append(sum)
d = 0
for i in range(len(sumfactors)):
    if sumfactors[i] == max(sumfactors):
        d = i
        break
print(factors[d])
