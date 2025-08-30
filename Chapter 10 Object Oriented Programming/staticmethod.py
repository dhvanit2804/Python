'Static Methods is a method that belongs to the class rather than any object instance.'

'''Sometimes we need a function that does not use the self-parameter. We can define a 
static method using the @staticmethod decorator'''

class Employee:
    language = "Python" # Class attribute
    salary = 1200000
    company = "Google"

    'This is a method of the Employee class.'
    def getInfo(self):
        print(f"The Language is {self.language}. The Salary is {self.salary}.")
    
    @staticmethod
    def greet():
        print("Good Morning!")


dhvanit = Employee()
dhvanit.language = "React"

dhvanit.greet()
dhvanit.getInfo()