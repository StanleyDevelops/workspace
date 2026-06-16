import re

# Extract all numbers from: "abc123xyz456"
text1 = "abc123xyz456"
print(re.findall(r"\d+", text1))

# Validate a Gmail address
text2 = "stanleykerketta777@gmail \
    bahalenkerketta03@gmail.com \
    niral.kerketta64@gmail.com\
    25btcse005@shiats.edu.in\
    stanleykerketta09@gmail.com"

print(re.findall(r"\w+@\w+.\w+", text2))     #couldn't catch '.' in niral.kerketta

# Extract all hashtags from: 
text3 = "#python #coding #AI love hate"
print(re.findall(r"#\w+", text3))

# Extract all 10-digit phone numbers.

text = "98101188870 852784944 9012802938 871 87 3"
print(re.findall(r"\d{10}", text))                    #r"\b\d{10}\b"  word boundary

