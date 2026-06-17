import json

# from python to json string
data = {
    "name": "Lee",
    "age": 19
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

# from json string to python

json_data = '{"name": "Lee", "age": 19}'
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))

# formatting
my_data = {"name": "Kerketta","age": 20,"hobby": "codin", "gender": "male"}

print(json.dumps(my_data, indent=2))

# writing json to a file 

data = {"phone": 981013922, "email": "stanleykerketta777@gmail.com"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading json from a file
with open("data.json", "r") as file:
     love = json.load(file)

print(love)

# Nested Json
your_data = {
     "user": {
          "name": "Stanley",
          "age": 19     },
     "skills":[ 
          "C++",
          "Java",
          "Python"
     ]
}

print(your_data['skills'])
print(your_data['user']['age'])

# Conversion of None and True/False from python to json
her_data = {"name": "priya",
            "age": 20,
            "active": True,
            "job": None}
print(json.dumps(her_data))





