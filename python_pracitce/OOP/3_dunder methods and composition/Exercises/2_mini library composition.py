# Mini library using composition

# Book class
class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} [ISBN: {self.isbn}]"

# Member class
class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title} by {book.author}")

    def return_book(self, book):
        self.borrowed_books.remove(book)
        print(f"{self.name} returned {book.title} by {book.author}")

    def show_borrowed(self):
        print(f"Books Borrowed: ")
        for book in self.borrowed_books:
            print(f" --{book.title} by {book.author}")


# Library Class 
class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to {self.name}")

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} added to {self.name} as a member")

    def show_books(self):
        for book in self.books:
            print(f" --{book.title} by {book.author}")

    def show_members(self):
        for member in self.members:
            print(f" - {member.name}")

    def lend_book(self, book, member):
        if book in self.books:
            self.books.remove(book)   # remove from library
            member.borrow(book)       # add to member
        else:
            print(f"{book.title} is not available.")
            

# book objects
b1 = Book("Money Maker", "Arthur", "IND9090")
b2 = Book("Code for Life", "Robert", "SWL234")
print(b1,b2)

# member objects
m1 = Member("Lee", "A23")
m2 = Member("Peter", "D18")

lib1 = Library("Central Library")
lib1.add_member(m1)
lib1.add_member(m2)
lib1.add_book(b1)
lib1.add_book(b2)
lib1.show_books()
lib1.show_members()

lib1.lend_book(b1, m1)
lib1.lend_book(b1, m2)



    

    
        
        