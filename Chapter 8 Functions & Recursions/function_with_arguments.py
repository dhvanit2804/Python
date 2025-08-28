'''A function can accept some value it can work with. We can put these values in the 
parentheses.'''

def greet_user(name, ending):
    print("Good day " + name)
    print(ending)
    return "Ok"

greet_user("Dhvanit", "Thank You")
greet_user("Rohan", "Dhanyvaad")

a = greet_user("Rahul", "Thanks") # This will call the function and store the return value in 'a'
print(a)