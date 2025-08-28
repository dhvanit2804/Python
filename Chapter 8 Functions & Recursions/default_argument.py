'We can have a value as default as default argument in a function.'
'In This example, the function greet_user has a default argument for ending'

def greet_user(name, ending="Thank You"):
    print("Good day " + name)
    print(ending)
    return "done"

greet_user("Dhvanit")
greet_user("Rohan", "Dhanyvaad") # Here we are overriding the default argument