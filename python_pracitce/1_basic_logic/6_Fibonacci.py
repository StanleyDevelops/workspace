# Non-recursive Fibonacci Sequence

a = 0
b = 1
print(a,b)     

i=0
while i<10:    # but this logic prints 12 terms (two extra)
    c = a + b
    print(c)
    a = b
    b = c 
    i +=1


# Logic-Fixed code
a, b = 0, 1

for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b



