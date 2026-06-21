# with open()
with open("hobbies.txt", "a+") as file:
    file.write("Football")

# append
file = open("notes.txt", "a")
file.write("\nRuby")
file.close()

# r+ 
file = open("programs.txt", "r+")
file.read()
file.write("\nGolang")
file.close()

# w+
file = open("notes.txt", "w+")
file.write("\nPython")
print(file.read())
file.close()

# binary files - returns <bytes>
with open("photo.jpg", "rb") as source:
    data = source.read()

with open("copy.jpg", "wb") as destination:
    destination.write(data)


