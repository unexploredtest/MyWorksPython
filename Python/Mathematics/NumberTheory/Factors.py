# For a given number, it'll give a list of its factors.

r = "If you want to try another integer, press Enter"
r += ", if finished, press any other key:"

while True:
    a = int(input("What number would you like to see its factors?"))
    factors = [1]
    i = 2
    while i <= a / 2:
        if a % i == 0:
            factors.append(i)
        i += 1
    factors.append(a)
    print(f"Here are the factors of {a}:")
    print(f"{factors}")
    z = input(f"{r}")
    if z == "":
        continue
    else:
        break
