# Simple program to check weather entered character is vowel or constant
# logic confusion, used loop instead of simple logic


char = input("Enter a character: ").lower()
length  = len(char)

if length == 1 and char.isalpha():   #alnum() to rule out numbers and symbols
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:         # python membership operator to check instantly
        print("A vowel man!")
    else:
        print("It's a constant")
    
else:
    print("Please enter a single english alphabet.")
    

