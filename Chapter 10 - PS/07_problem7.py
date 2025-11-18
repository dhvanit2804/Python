'Create a class Student with attributes name and marks. Create an object and print the details.'

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_name(self):
        print(f"Hello My Name is {self.name}")

    def get_marks(self):
        print(f"My Marks is {self.marks}")

s1 = Student("Dhvanit", 87)

s1.get_name()
s1.get_marks()