# Mini Project - Student report system

def calculate_total(marks: list[int]) -> int:
    return sum(marks)

def calculate_average(marks: list[int]) -> float:  
    if not marks:
        raise ValueError("The list is empty!")
    return sum(marks)/len(marks)

def find_highest(marks: list[int]) -> int:
    return max(marks)

def generate_report(name: str,
                    marks: list[int]):
    print(f"Student: {name}")
    print(f"Marks: {marks}") 

    print(f"Total:{calculate_total(marks)} ")
    print(f"Average: {calculate_average(marks)}")
    print(f"Highest: {find_highest(marks)}")

generate_report("Stanley", [99,77,57,98,67])


     