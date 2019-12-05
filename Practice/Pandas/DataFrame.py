
import numpy as np
import pandas as pd

classSM102Sa = pd.Series(["Persian", "Physics", "Geography", "English"],
               index=["First", "Second", "Third", "Forth"])

classSM102Su = pd.Series(["Writing", "Physics", "Geometry", "Sport"],
               index=["First", "Second", "Third", "Forth"])

classSM102Mo = pd.Series(["Chemistry", "Chemistry", "Mathematics", "Mathematics"],
               index=["First", "Second", "Third", "Forth"])

classSM102Tu = pd.Series(["Physics", "Arabic", "Laboratory", "Meditation"],
               index=["First", "Second", "Third", "Forth"])

classSM102We = pd.Series(["Mathematics", "English", "Religion", "Defense"],
               index=["First", "Second", "Third", "Forth"])


classSM102 = pd.DataFrame([classSM102Sa, classSM102Su, classSM102Mo, classSM102Tu,classSM102We],
               index=["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"])


classSM102.head()

classSM102.loc["Monday"]
classSM102.loc["Monday"].loc["Second"]
classSM102.loc["Monday", "Second"]

classSM102.iloc[2]
classSM102.iloc[2].iloc[2]

classSM102["First"]

classSM102.T

classSM102.loc[:, ["First", "Second"]]

classSM102_2 = classSM102.drop(["Saturday", "Wednesday"])
classSM102_2.head()
