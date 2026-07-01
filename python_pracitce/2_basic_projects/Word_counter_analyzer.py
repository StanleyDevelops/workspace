# Simple program that analyse
# Total words
# Total characters
# Number of vowels
# Longest word
# Did in first attempt: Good {took 1.5 hours}

para = input("Write a paragraph or sentence: ").lower().strip()

words = para.split()

if len(words) == 0:
    print("No input given!")
else:
    print("The Number of words:", len(words))

    # For characters and vowels
    total_char = 0
    vowel_count = 0
    vowels = ["a", "e", "i", "o", "u"]

    for word in words:
        for char in word:
            total_char += 1

            if char in vowels:
                vowel_count += 1

    print(f"Total characters: {total_char}")
    print(f"No of vowels: {vowel_count}")

    # For longest word
    longest_word = words[0]

    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word

    print("The longest word:", longest_word)




