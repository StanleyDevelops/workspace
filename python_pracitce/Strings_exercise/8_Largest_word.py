# Program to print the largest word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split(" ")

max_word = words[0]
for word in words[1:]:
    if len(word) > len(max_word):
        max_word = word

print("The Max. length word is: ", max_word)










        