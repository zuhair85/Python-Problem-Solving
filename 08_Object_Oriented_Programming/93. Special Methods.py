# Problem statement
# Create a Book class that implements Python's three special methods: __str__, __repr__, and __eq__.
#
# Your class should represent a book with a title, author, and publication year.
# Requirements
# Your Book class must:
# 1. Accept title, author, and year when creating a book.
# 2. Implement __str__ to return a human-readable description of the book.
# 3. Implement __repr__ to return an unambiguous representation that resembles valid Python code for recreating the object.
# 4. Implement __eq__ to determine whether two books are equal.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    #We can return a string representation of the object when we print it directly to the console
    def __str__(self):
        return f'{self.title} by {self.author} ({self.year})'

    #Return an unambiguous representation that resembles valid Python code for recreating the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        else:
            return self.title == other.title and self.author == other.author and self.year == other.year

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Animal Farm", "George Orwell", 1945)

print(book1)

print(repr(book1))
# Book('1984', 'George Orwell', 1949)

print(book1 == 100)

print(book1 == book2)
print(book1 == book3)