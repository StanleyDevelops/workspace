# Finding all substring 
# Using nested loop and string slicing
# hard think
string = "abc"
length = len(string)

for i in range(length):
    for j in (i+1, length +1):
        sub_string = string[i:j]
        print(sub_string)



        