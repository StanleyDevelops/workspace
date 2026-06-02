# Call keyword using diferent order

def book(title,author,pages):
    """The function has 3 parameter:
    Title: user gives the tile
    author: who wrote it
    pages: no of pages"""

    print(f"The Author: {author}")
    print(f"Title: {title}")
    print(f"No. of Pages: {pages}")

print(book.__doc__)
book("The Game of Stones", 1, "Master Lee")

# Call using positional and keyword argument
def rectangle(length, width):
    return f"The Area is: {length*width}"

print(rectangle(18, width = 90))
print(rectangle(78,23))
print(rectangle(width = 2, length = 3))

# Mixing positional, keyword and default arguments 
def create_account(username, role ="user"):
    print(f"Username: {username}")
    print(f"Role: {role}")

create_account("Stanley")
create_account("Donnie", role = "Commander")
create_account("Shreya", "manager")
