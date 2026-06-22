# import csv module and read a file 
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)     #python shows a list of rows

# without the header
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# writing to a csv file
with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Andrew", 13, "Chemistry"])

# writerows()
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    rows = [
        ["Name", "age", "branch"]
        ["stanley", "19", "CSE"]
        ["Luke", "90", "BSC"]
    ]

    writer.writerows(rows)

# DictReader 
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        
# DictWriter
with open("students.csv","w",newline="") as file:

    fields = ["Name","Age","Branch"]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()
    writer.writerow({
        "Name":"Lee",
        "Age":20,
        "Branch":"CSE"
    })
    writer.writerow({
        "Name":"John",
        "Age":21,
        "Branch":"ECE"
    })