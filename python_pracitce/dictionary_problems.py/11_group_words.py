# Group words by first letter

list_main = ["apple","ant","ball","bat"]

l1 = []
l2 = []
for i in list_main:
    if i[0][0] == 'a':
        l1.append(i)
print(l1)
                                                        # manually hardcoding is stidiuos
for i in list_main:
    if i[0][0] == 'b':
        l2.append(i)
print(l2)

d1 = {'a': l1,
      'b': l2}
print(d1)

# Dynamic way
list_main = ["apple","ant","ball","bat","cat","dog","elephant"]
d1 = {}

for word in list_main:
    first_letter = word[0]
    if first_letter not in d1:
        d1[first_letter] = []

    d1[first_letter].append(word)

print(d1)
    


