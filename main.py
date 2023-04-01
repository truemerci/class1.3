class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.title

    def __lt__(self, other):
        return self.pages < other.pages


book1 = Book("Backend", "D.Ladylike", 35)
book2 = Book("JavaScript", "J.Rouse", 256)
book3 = Book("ProPython", "V.Ushakov", 157)

books = [book1, book2, book3]

print(f'{book1}\n{book2}\n{book3}')

print(len(book1), len(book2), len(book3))

print(book1 == book2)

for i in sorted(books):
    print(i)

if book1 in books:
    print("This book is on the list")
else:
    print("This book is not on the list")

print(max(books))
print(min(books))
