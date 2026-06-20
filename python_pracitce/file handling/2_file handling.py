# read mode in detail
file = open("notes.txt", "r")
print(file.read(6))     # reads n characters
print(file.read())
print(file.tell())      # where is the cursor
print(file.seek(0))     # moves the cursor
print(file.read(12))
file.close()

# readline
file = open("notes.txt", "r")
print(file.readline())
print(file.readline())
print(file.readlines())      # returns aa liness as a list, \n as a character
file.close()

# preferred way for large files
file = open("notes.txt", "r")
for line in file:
    print(line, end ="")
file.close()

# Writing files
file = open("programs.txt", "w")
file.write("Hello")
print(file.write("Hi"))      # returns a number of characters
file.close()

# writelines()
file = open("programs.txt", "w")
languages = ["Javascript\nCSS\nHTML"]
file.writelines(languages)
file.close()


