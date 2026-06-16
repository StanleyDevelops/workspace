import re

# search()
text1 = "I like programming in python"
result = re.search("python", text1)

print(result.start())
print(result.group())
print(result.end())

# re.findall()

text2 = "cat bat mat bol col mol dat"
matches = re.findall("at", text2)
print(matches)

# Find all digits

text3 = "123 567 890"
numbers = re.findall(r"\d+", text3)
print(numbers)

# re.match - checks the beginning of the string

my_text = "python is powerful and easy too"
result = re.match("python", my_text)
if result:
    print(f"Found 'python'")
else:
    print(f"Couldn't find 'python'")

# Special Characters
print(re.findall(r"\d", "123abc"))
print(re.findall(r"\D", "345abc"))
print(re.findall(r"\w", "123_abc"))         # includes alphabets,  numbers, underscore
print(re.findall(r"\W", "gmail@.com"))      # non-words
print(re.findall(r"\s", "Hi there"))        # whitespace
print(re.findall(r"\S", "Hi there"))


# Quantifiers - +,*

print(re.findall(r"ab*", "a ab abb abcdf ablove"))           # zero or more occurance
print(re.findall(r"colou?r", "color colour"))                # zero or one occurance
print(re.findall(r"\d{4}", "123 3456 1 2341"))               # exactly n occurance
print(re.findall(r"\d{2,4}", "1 2 4 34 323 1234 1214 1"))    # min and max 


# Character sets
print(re.findall(r"[abc]", "apple banana cat"))
print(re.findall(r"[A-Z]", "Python JAVA C"))                 # range

# Anchors
print(re.findall(r"^love", "love is all I have, for you"))   # start
print(re.findall(r"you$", "love is all I have, for you"))    # end

# re.sub()   - substitute or replace
your_text = "I love JAVA language"
print(re.sub("JAVA", "C++", your_text))

# Extract Email Address
text = """abc@gmail.com xyz@yahoo.com"""
emials = re.findall(r"\w+@\w+.\w+", text)
print(emials)

import re

# Password validation

password = input("Enter password: ")

if re.search(r"[A-Z]", password) and \
   re.search(r"[a-z]", password) and \
   re.search(r"\d", password):

    print("Strong Password")
else:
    print("Weak Password")