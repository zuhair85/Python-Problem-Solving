# Task: Create two classes, Book and Library, that support adding, searching, and listing books.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book objects can be added!")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.year})")

library = Library()

book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Clean Code", "Robert C. Martin", 2008)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

result = library.search_book("1984")
print(result.title)