# Here, I'll try to make a class for names

class Name:
    place = "Universe"
    def __init__(self, name, age, gender, origin, major):
        self.age = f"{age}"
        self.gender = f"{gender}"
        self.origin = f"{origin}"
        self.name = f"{name}"
        self.major = f"{major}"
    def about(self):
        return f"Hello, I am {self.name} and I am {self.age}, I majored in {self.major}."
    @classmethod
    def loc(cls):
        return f"The name is in the {cls.place}"
    @staticmethod
    def lol(where):
        return f"He/She/It is in/at/on {where} now."
