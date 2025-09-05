'What is multiple inheritance in Python?'
'Multiple inheritance is a feature in OOP where a class can inherit attributes and methods from more than one parent class.'
'This allows for the creation of a new class that combines the functionality of multiple existing classes.'

class Employee:
    company = "ITC"
    name = "Dhvanit"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all languages, your favorite language is {self.language}")

'This is multiple inheritance in Python'
class Programmer(Employee, Coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.company} he is good in {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showlanguage()