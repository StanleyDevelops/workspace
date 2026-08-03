# Correct Library composition

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []       # Library has books, stored as a list

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to {self.name}")

    def show_books(self):
        if not self.books:
            print("No books in library")
            return
        print(f"---------{self.name}--------")
        for book in self.books:
            print(f" - {book}")      # calls Book's __str__


book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Atomic Habits", "James Clear")
book3 = Book("Clean Code", "Robert Martin")

lib = Library("City Library")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.show_books()


        
        