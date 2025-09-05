'''What is Operator Overloading?

In Python, operators like +, -, *, /, etc., are special methods (also called magic methods or 
dunder methods like __add__, __sub__, __mul__, etc.).
Operator Overloading means giving new meaning to these operators for user-defined classes.'''

'''Operators in Python can be overloaded using dunder methods. 
These methods are called when a given operator is used on the objects.'''

class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, num):
        return self.n + num.n

n = Number(5)
m = Number(10)

print(n + m)