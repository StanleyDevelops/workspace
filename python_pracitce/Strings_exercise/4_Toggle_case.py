# Without swapcase() toggle the letters

string = "pyThOn"
toggled_string = ""
for char in string:
    if char.islower():       #Strings are immutable
        toggled_string += char.upper()     #you  tried changing in loop
    else:
        toggled_string += char.lower()
print(toggled_string)
