'What is Constructor?'
'A constructor is a special method that is automatically called when an object of a class is created.'
'It is used to initialize the attributes of the class.'
'It is defined using the __init__() method.'

class Employee:
    language = "Python" # Class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an Employee object.")
    
    def getInfo(self):
        print(f"The Language is {self.language}. The Salary is {self.salary}.")
    
    @staticmethod
    def greet():
        print("Good Morning!")


dhvanit = Employee("Dhvanit", 1300000, "JavaScript")

print(dhvanit.name)
print(dhvanit.language)
print(dhvanit.salary)

# rohan = Employee()