import json

# writing json to a file
data = {"name": "stanley","age": 19,"branch": "CSE","skill": ["Java","React","Django"]}
with open("myskill.json", "w") as file:
    json.dump(data, file, indent=4)  # use indent 2 or 4

# reading a json text
with open("myskill.json", "r") as file:
    data = json.load(file)
    print(data)

# preserving unicode
student = {"name": "ली"}
with open("student.json", "w") as file:      # ensure ascii
    json.dump(student,file, indent=2, ensure_ascii=False)

# Standard process to update a file in json

with open("notes.txt", "r") as file:
    data = json.load(file)

data["age"] = 20      # uodated the data

with open("notes.json", "w") as file:
    json.dump(data, file, indent=2)   # writing to json file again 


# adding and removing keys
data["city"] = "Ranchi"
del data['city']