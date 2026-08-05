# Complete Library System

class Book:

    # Constructor
    def __init__(self, title, author,isbn, is_available = True):   # defining instance attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):            # for others
        return f"{self.title} by {self.author} [ISBN: {self.isbn}] - {"Available" if self.is_available else "Not available"}"

    def __repr__(self):           # for developers
        return f"Book(Title:{self.title}, Author: {self.author}, ISBN: {self.isbn}, Available={self.is_available})"

class Member:

    def __init__(self, name, member_id):       
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []    # contains the books borrowed by member

    def borrow(self, book):
        self.borrowed_books.append(book)         # adds book to the member borrowed list
        book.is_available = False         
        print(f"{self.name} borrowed {book.title} by {book.author}")

    def return_book(self, book):
        self.borrowed_books.remove(book)                  # removes book from memeber borrowed list
        book.is_available = True        
        print(f"{self.name} returned {book.title} by {book.author}")

    def show_borrowed(self):
        for i,book in enumerate(self.borrowed_books):
            print(f"{i+1}. {book.title} by {book.author}")

    def __str__(self):
        return f"Member(Name: {self.name}, ID: {self.member_id}, No. of book borrowed: {len(self.borrowed_books)})"


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []                   # to store books
        self.members = []                 # to store members

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} added to {self.name}")

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} added to {self.name}")

    def lend_book(self, book, member):
        if book.is_available:                  
            member.borrow(book)                   # borrow() sets is_available = False
        else:
            print("Book not available")

    def accept_return(self, book, member):
        self.books.append(book)
        member.return_book(book)                  

    def show_available_books(self):               
        for i, book in enumerate(self.books):
            if book.is_available == True:                # shows all the books available in library book list
                print(f"{i+1}. {book}")

    def show_members(self):
        for i, member in enumerate(self.members):
            print(f"{i+1}. {member}")

    def __str__(self):
        return f"Library(Name: {self.name}, No. of books Available: {len(self.books)}, Total Members: {len(self.members)})"
        

# Test objects

# setup
b1 = Book("The Alchemist", "Paulo Coelho", "ISBN001")
b2 = Book("Atomic Habits", "James Clear", "ISBN002")
b3 = Book("Clean Code", "Robert Martin", "ISBN003")

m1 = Member("Stanley", "M001")
m2 = Member("Rahul", "M002")

lib = Library("City Library")

# adding books and members
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_member(m1)
lib.add_member(m2)

# lend books
lib.lend_book(b1, m1)
lib.lend_book(b2,m2)
lib.lend_book(b1, m2)       # prints book not available

# show state
lib.show_available_books()         # only b3 book is left
m1.show_borrowed()
m2.show_borrowed()

# return
lib.accept_return(b1,m1)
lib.show_available_books()       # Now b1 and b3 is available


        
        