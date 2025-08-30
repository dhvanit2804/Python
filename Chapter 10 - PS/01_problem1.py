'''Create a class “Programmer” for storing information of few programmers 
working at Microsoft. '''

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
    
    def displayInfo(self):
        print(f"{self.name} works at {self.company} as a {self.position} with a salary of {self.salary}")

    
programmer1 = Programmer("Dhvanit", 1400000, "Python Developer")
programmer1.displayInfo()