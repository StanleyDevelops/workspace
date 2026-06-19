# 1
from collections import Counter

sentence = "the quick brown fox jumps over the lazy dog the fox runs"
my_counter = Counter(sentence.split())
print(my_counter)

# 2
from collections import defaultdict

records = [("Alice", 85), ("Bob", 72), ("Alice", 90), ("Charlie", 88), ("Bob", 95)]
my_dict = defaultdict(list)
for student , mark in records:
    my_dict[student].append(mark)

print(dict(my_dict))

# 3 
from collections import deque
def add_elements(my_list: list):
    the_deque = deque([],maxlen=3)
    for i in my_list:
        the_deque.append(i)

    return list(the_deque)
        
print(add_elements([1,2,3,4,5,6]))

# 4
from collections import namedtuple

student = namedtuple("Students",["name", "age", "grade"])
children = student("stanley", 19, "A"), student("matthew", 18, "B")

def check_student(child):
    return child.grade == "A"

print(check_student(children[0])) 
print(check_student(children[1])) 
