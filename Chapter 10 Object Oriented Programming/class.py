'What is Object Oriented Programming?'
'Object Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", '
'which can contain data and code: data in the form of fields (often known as attributes or properties), '
'and code, in the form of procedures (often known as methods).'

'Class is a blueprint for creating objects'
'Objects are instances of classes.'
'When Class is defined, no memory is allocated until an object is created.'

class Employee:
    language = "Python"
    salary = 1200000
    company = "Google"

dhvanit = Employee()
dhvanit.name = "Dhvanit Parate"
print(dhvanit.name, dhvanit.language, dhvanit.salary, dhvanit.company)

rahul = Employee()
rahul.name = "Rahul"
print(rahul.name, rahul.language, rahul.salary, rahul.company)