'Create a class Employee with constructor that initializes id, name, and salary.'

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def showinfo(self):
        print(f"Hello! My ID number is {self.id}, my name is {self.name}, "
              f"I am working as a Python developer, and my salary is {self.salary}.")

e = Employee(28, "Dhvanit", 40000)
e.showinfo()