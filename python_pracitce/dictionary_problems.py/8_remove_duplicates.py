# Remove duplicate values

_diction = {
        "a":1,
        "b":2,
        "c":1
        }

clean_dict = {}
seen_values = set()

for key, value in _diction.items():
    if value not in seen_values:
        clean_dict[key] = value
        seen_values.add(value)

print(clean_dict)
