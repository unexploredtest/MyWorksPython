import csv

with open("data.csv", "r") as data:
    csv_data = csv.DictReader(data)

    print("0.8")
    print(next(csv_data)["0.8"])
    print(next(csv_data)["0.8"])
    print(next(csv_data)["0.8"])
    print(next(csv_data)["0.8"])
    print(next(csv_data)["0.8"])
    print(next(csv_data)["0.8"])
    print("The first result finished.")

with open("data.csv", "r") as data2:
    csv_data2 = csv.reader(data2)
    lines = []
    for line in csv_data2:
        lines.append(line)

    for i in range(7):
        print(lines[i][-1])
    print("The second result finished.")
