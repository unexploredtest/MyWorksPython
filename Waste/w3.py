class Book:
    def __init__(self, subject, title, author, pages):
        self.title   = title
        self.author  = author
        self.pages   = pages
        self.subject = subject

    def Information(self):
        print(f'"{self.title}" is written by {self.author} Which is about {self.subject}. It has {self.pages} pages.')

Thomas_Calculus = Book("mathematics", "Thomas Calculus", "George Thomas", 1204)

Thomas_Calculus.Information()
