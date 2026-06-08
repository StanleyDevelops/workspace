# Zip() is used to combine two or more elements index by index

# 1 - You have two lists — ["a", "b", "c"] and [1, 2, 3]. Zip them into a list of tuples.
lis1 = ["a", "b", "c"]
lis2 = [1, 2, 3]
print(dict(zip(lis1,lis2)))

# 2 - Given names = ["Alice", "Bob", "Charlie"]
#  and scores = [85, 92, 78], print only the names where the score is above 80.

name = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in list(zip(name, scores)):
    if score >=80:
        print(f"{name}: {score}")

# 3 

subjects = ["Math", "Science", "English"]
marks = [88, 95, 70]
passed = [True, True, False]
for subject, mark, status in zip(subjects, marks, passed):
    print(f"{subject}: {mark}  ({status})")
