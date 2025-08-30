'Self is a reference to the current instance of the class.'
'It is automatically passed with a function call from an object.'

'If We Create Method in Class but dont Pass Self Parameter it will throw an error'

class Employee:
    language = "Python" # Class attribute
    salary = 1200000
    company = "Google"

    'This is a method of the Employee class.'
    def getInfo(self):
        print(f"The Language is {self.language}. The Salary is {self.salary}.")
    
    def greet(self):
        print("Good Morning!")


dhvanit = Employee()
dhvanit.language = "React"

dhvanit.greet()
dhvanit.getInfo() # This will print the updated language and salary
# Employee.getInfo(dhvanit)

"These Both Above Calls are Valid"