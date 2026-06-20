# read an exisiting file
try:
    file = open("notes.txt", "r")
except FileNotFoundError as e:
    print(f"{e}")

print(file.read())
file.close()

# append into a file
file = open("students.txt", "a")
file.write("\nDo you like DSA?!")
file.close()

# writing into a new file
file = open("test.txt","w")
file.write("This is a new file")
file.write("\nPython is a procedural language")
file.close()

# exclusive creation
try:
    file = open("unique.txt", "x")
except FileExistsError as e:
    print(f"{e}")

