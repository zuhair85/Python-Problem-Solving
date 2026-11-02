# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# 		        They are automatically called by many of Python’s built-in operations.
# 		        They allow developers to define or customize the behavior of objects.

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    #We can return a string representation of the object when we print it directly to the console
    def __str__(self):
        return f'{self.title} by {self.author}'

    #Check if two objects (books) are equal
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    #Lets us compare num_pages using less than (<) operator
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    #Customize the behavior of addition operator between two books
    #We will be adding num_pages of two books
    def __add__(self, other):
        return f'{self.num_pages + other.num_pages} pages'

    #Search for a keyword in an object
    def __contains__(self, item):
        return item in self.title or item in self.author

    #Seach for a key given an object
    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f'Item {item} was not found'

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Warrior", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 176)


print(book1)
print(book1 == book2)
print(book1 == book4)
print(book3 < book2)
print(book2 + book1)
print('Lion' in book3)
print(book1["author"])
print(book3["num_pages"])
print(book4["audio"])
