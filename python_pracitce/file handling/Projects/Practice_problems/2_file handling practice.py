# Write find_line(filename, keyword) → returns line numbers (1-indexed) where keyword appears, case-insensitive.

def find_line(filename, keyword):
    with open(filename, "r") as file:
        for i,line in enumerate(file):
            if keyword in line:
                print(i+1)
find_line("notes.txt", "OOP")

    
