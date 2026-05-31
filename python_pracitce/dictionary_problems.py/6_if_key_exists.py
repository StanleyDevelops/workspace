# if key exists without in

d1 = {'rahul': 43,
      'raghav': 56,
      'rajeev': 67}

find = 'ram'
found = False
for key in d1:
    if key == find:
        print(f"{key} is present")
        found = True

if not found:
    print("Not found!")

# better Time Complexity way 
d1 = {'rahul': 43,
      'raghav': 56,
      'rajeev': 67}
find = 'ram'

result = d1.get(find, None)

if result is not None:
    print(f"{find} is present with value {result}")
else:
    print(f"{find} doesn't exist!!")

# try-except method
d1 = {'rahul': 43,
      'raghav': 56,
      'rajeev': 67}
find = 'ram'
try:
    value = d1[find]
    print(f"{find} is present in the dictionary")
except KeyError:
    print(f"{find} doesn't exists")





