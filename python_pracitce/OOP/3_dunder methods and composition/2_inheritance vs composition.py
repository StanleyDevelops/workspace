# Inheritance vs Composition

# Wrong approach for Library - inheritance
class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author

class Library(Book):      # wrong - Library is NOT a Book
    pass
        
# A Library contains Book