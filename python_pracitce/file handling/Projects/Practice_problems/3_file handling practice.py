# Create students.csv with headers name, roll_no, marks and write 5 rows using csv.Dictwriter.

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        if int(line['marks']) < 80:
            print(line)
    

            
    

