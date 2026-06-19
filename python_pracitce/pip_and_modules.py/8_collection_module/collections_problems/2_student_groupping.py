# Student Grouping
# Group students by department using defaultdict(list)

from collections import defaultdict

students = [
    ("ECE", "Tom"),
    ("CSE", "Stanley"),
    ("EE","Micheal"),
    ("CSE", "Andrew")
]

def_dict = defaultdict(list)
for department, name in students:
    def_dict[department].append(name)

print(def_dict)
    