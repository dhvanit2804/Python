'What is Super() in Python?'
'Super() is a built-in function in Python that allows you to call methods from a parent class in a child class.'
'It is commonly used in inheritance to access and extend the functionality of the parent class.'

'super() method is used to access the methods of a super class in the derived class.'

class Employee:
    def __init__(self):
        print("Constructor is Employee class")
    a = 10

class Programmer(Employee):
    def __init__(self):
        print("Constructor is Programmer class")
    b = 20

class Manager(Programmer):
    def __init__(self):
        super().__init__() # This will call the constructor of Parent class
        print("Constructor is Manager class")
    c = 30

o = Employee()
print(o.a)

p = Programmer()
print(p.a, p.b)

m = Manager()
print(m.a, m.b, m.c)