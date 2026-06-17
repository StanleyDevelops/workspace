import json

# 1 Parse it and print the average of the marks.
pythondata = '{"student": {"name": "Raj", "marks": [85, 90, 78]}}'
read_data = json.loads(pythondata)
marks = read_data['student']['marks']
avg = sum(marks) / len(marks)
print(avg)

# 2 Create a dict with your own profile info
my_profile = {"name": "stanley",
              "age": 19,
              "skills": ["C++", "Kubernetes", "Pandas", "numpy"]}

with open("profile.txt", "w") as file:
    json.dump(my_profile, file, indent=4)

with open("profile.txt", "r") as file:
    read_data = json.load(file)

print(read_data)

# 3 Write a function save_data(data, filename) that takes any dict and filename.
import json
from pathlib import Path
def save_data(data: dict, filename: str):
    folder = Path.home() / "Desktop" / "python_test" / "json_folder"
    folder.mkdir(exist_ok=True)

    path = folder / filename
    try:
        with open(path, "w") as file:
            json.dump(data, file, indent=3)
    except Exception as e:
        print(f"File not saved: {e}")

save_data({"name": "niral", "age": 20}, 'my_info')  

# 4
contacts = [
    {"name": "Riya", "phone": "9876543210"},
    {"name": "Aman", "phone": "9123456780"}
]

with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent = 4)

with open("contacts.json", "r") as file:
    show =  json.load(file)

for item in show:
    print(item['name'])
