# print the temperature
import json
json_data = '{"city":"Delhi","temp":35}'
python_data = json.loads(json_data)
print(python_data['temp'])

# storing channel.json
my_data = {
    "channel": "Lee Codes",
    "subscribers": 10000
}

with open("my_data.json", "w") as file:
    json.dump(my_data, file, indent=4 )

# Given json_data = '{"name": "Alice", "age": 30, "city": "Mumbai"}', parse it and print only the name.
json_data = '{"name": "Alice", "age": 30, "city": "Mumbai"}'
py_data = json.loads(json_data)
print(py_data['name'])

