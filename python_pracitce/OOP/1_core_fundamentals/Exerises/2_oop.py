# Student class to demo getters and setters

class Student:

    def __init__(self):
        self.__marks = 0

    # getter - read only method
    def get_marks(self):
        return self.__marks
    
    # setter - controlled method to set balance
    def set_marks(self, mark):
        # validate before setting
        if mark < 0 or mark > 100:
            print("Invalid marks")
        else:
            self.__marks =  mark
            print(f"Marks set to: {mark}")

s = Student()
s.set_marks(95)
print(s.get_marks())
s.set_marks(150)        # validates marks
print(s.get_marks())




