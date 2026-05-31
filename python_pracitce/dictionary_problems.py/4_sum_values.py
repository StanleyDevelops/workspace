# Sum all dictionary values

diction_ = {
 "a":10,
 "b":20,
 "c":30
}

sum = 0 
for values in diction_.values():
    sum += values

print(f"The sum is: {sum}")
