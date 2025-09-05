'What is Inheritance?'
'Inheritance is a mechanism in OOP that allows a class to inherit attributes and methods from another class.'
'Inheritance is a way of creating a new class from an existing class.'

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} he is good in {self.language} language")

class Programmer(Employee):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.name} he is good in {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)