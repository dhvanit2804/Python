'Instance attributes, take preference over class attributes during assignment & retrieval.'

class Employee:
    language = "Python" # Class attribute
    salary = 1200000
    company = "Google"

dhvanit = Employee()
dhvanit.name = "Dhvanit Parate" # This is an instance attribute
dhvanit.language = "JavaScript" # This creates an instance attribute 'language' for dhvanit

print("Name:", dhvanit.name)
print("Language:", dhvanit.language)
print("Salary:", dhvanit.salary)
print("Company:", dhvanit.company)