# Reverse key-value pairs
# output {1:"a",2:"b"} 
d1 = {"a":1,"b":2}    
reversed_dic = {}
for key, value in d1.items():
    reversed_dic[value] = key

print(reversed_dic)

# short-cut

result = {value:key for key, value in reversed_dic.items()}
print(result)
