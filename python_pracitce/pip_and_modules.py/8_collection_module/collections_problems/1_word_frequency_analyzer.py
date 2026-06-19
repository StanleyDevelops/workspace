# 1. Word Frequency Analyzer
# Read a paragraph.
# Count each word using Counter.
# Display the 5 most common words.

from collections import Counter

def word_counter(words: str):
    frequency_dict = Counter(words.lower().strip().split())
    print(dict(frequency_dict))

    for word, count in frequency_dict.most_common(5):
        print(f"{word}: {count}")

my_word = '''Python is an amazing programming language. Learning Python helps with backend 
development, and Python processing speed is incredibly optimized with modules!'''
print(word_counter(my_word))

