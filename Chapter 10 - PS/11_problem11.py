'Create a class Person with a method greet() that prints “Hello, my name is ___”.'

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Dhvanit")
p.greet()
