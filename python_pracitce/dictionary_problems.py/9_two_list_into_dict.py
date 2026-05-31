# Convert two lists into dictionary
 
l1 = ["name","age"]
l2 = ["Lee",18]

d1 = {}
for i in range(0,2):
        d1[l1[i]] = l2[i]

print(d1)


# Using zip function

l3 = ['name','age']
l4 = ['kerketta', 40]

store = dict(zip(l3,l4))
print(store)


