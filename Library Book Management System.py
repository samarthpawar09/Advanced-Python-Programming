class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def category(self):
        if self.price >= 500:
            return "Premium"
        else:
            return "Standard"

    def display(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Price   :", self.price)
        print("Category:", self.category())
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nLibrary Book Records")
        print("=" * 30)
        for book in self.books:
            book.display()


library = Library()

n = int(input("Enter number of books: "))

for i in range(n):
    print(f"\nEnter details of Book {i+1}")
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))

    book = Book(book_id, title, author, price)
    library.add_book(book)

library.display_books()
