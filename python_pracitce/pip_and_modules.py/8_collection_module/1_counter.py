# counter class

from collections import Counter
text = "banana"
the_count = Counter(text)
print(the_count)

# With list 
list_1 = [1,2,3,2,2,3,1,2,3,3]
count = Counter(list_1)
print(count)

# access frequency
print(the_count['a'])
print(count[1])

# most_common() 
print(count.most_common())

# elements()
count = Counter(a=3,b=2)
print(list(count.elements()))

# update
count = Counter("Banana")
count.update("apple")
print(count)

# subtract
count = Counter("banana")
count.subtract("ana")
print(count)

# Arithmetic Operations
c1 = Counter(a=3,b=2)
c2 = Counter(a=1,b=5)
print(c1+c2)
print(c1-c2)    # 2-5=-3 excluded

# count word frequency
sentence = "python is fun and python is easy"
count = Counter(sentence.split(" "))
print(count)