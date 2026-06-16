import re

# Replace all spaces with _
text = "I really love python"
print(re.sub(r"\s+", "_", text))

# Count how many words are present in a sentence
text = "I like JAVA and C++ too"
count = len(text.split())
print(count)

# Validate whether a string starts with "https://"
string = "https://youtube.com  https://claude.ai"
hyperlinks = re.findall(r"https://\w+\.\w+", string)
print(hyperlinks)

# Extract all capitalized words from: 
my_text = "Python is Created By Guido Van Rossum and I"
words = re.findall(r"[A-Z]\w*", my_text)                        # * zero or more occurance
print(words)                                                    # + one or more



