'Self is a reference to the current instance of the class.'
'It is automatically passed with a function call from an object.'

class Employee:
    language = "Python" # Class attribute
    salary = 1200000
    company = "Google"


dhvanit = Employee()
dhvanit.name = "Dhvanit Parate" # This is an instance attribute
dhvanit.language = "JavaScript"