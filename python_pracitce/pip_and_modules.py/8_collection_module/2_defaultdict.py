from collections import defaultdict

d = defaultdict(int)
d["math"]
d["english"] += 5
print(d)

# append()

students = defaultdict(list)
students["python"].append("Lee")
students["python"].append("Stanley")
print(students)

# using a set 
courses = defaultdict(set)
courses['python'].add("Lee")
courses['python'].add('Lee')
print(courses)

# grouping example
data = [("python", "Lee"),
        ("Java", "Tom"),
        ("python", "Sam")]

group = defaultdict(list)
for course , student in data:
    group[course].append(student)

print(group)

# Group students by department.

students = [
("CSE","Lee"),
("ECE","John"),
("CSE","Alex"),
("ME","David")
]

group = defaultdict(list)

for depart, student in students:
    group[depart].append(student)

print(group)

