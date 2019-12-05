
import pandas as pd

numbers = [5, 6, 8, 33, 87]
windows = ["XP", "Vista", "7", "8", "8.1", "10"]

Pnumbers = pd.Series(numbers)
print(Pnumbers)

Pwindows = pd.Series(windows)
print(Pwindows)


Pprimes = pd.Series([2,3,5,7], index=["first", "second", "third", "forth"])
print(Pprimes)

print(Pwindows.iloc[1])
print(Pprimes.loc["second"])


cd_1 = pd.Series(["2019", 10, 3], index=["release", "price", "size"])
cd_2 = pd.Series(["2014", 5, 4], index=["release", "price", "size"])
cd_3 = pd.Series(["2017", 20, 7], index=["release", "price", "size"])

cds = pd.DataFrame([cd_1, cd_2, cd_3], index=["CD 1", "CD 2", "CD 3"])

cds.head()

cds.loc["CD 3"]
cds["price"]
