class prime:

    brothers = "Primes have an infinite brothers(primes)."

    def __init__(self, number):
        if number == 2:
            numberity = "even"
        else:
            numberity = "odd"
        self.factors = f"{number} factors are 1 and {number}."
        self.oe = f"{number} is {numberity}."
    @classmethod
    def Wfactors(cls):
        return f"Because according to the definition, {cls.brothers}"


a = prime(7)
print(a.factors)
print(a.oe)
print(a.brothers)
print(a.Wfactors())

b = prime(2)
print(b.oe)
print(b.brothers)
print(b.Wfactors())
