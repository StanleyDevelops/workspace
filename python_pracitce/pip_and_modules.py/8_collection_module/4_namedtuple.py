from collections import namedtuple

Student = namedtuple("my_info", ["name","age","branch"])
s = Student("Lee", 20, "CSE")
print(s)
print(s.name)
print(s.age)

# _asdict()
print(s._asdict())

# _replace()
print(s._replace(age=21))

# Example
employee = namedtuple("employee", ['id','name','salary'])
e = employee("1A","Tommy",90000)
print(e)
