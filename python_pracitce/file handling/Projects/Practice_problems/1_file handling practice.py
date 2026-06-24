# Write count_words(filename) → returns total word count.

def count_words(filename):
    with open(filename, "r") as file:
        words = file.readlines()
        total = 0
        for i in words:
            word = i.split()
            total += len(word)

        print(total)
count_words("notes.txt")
