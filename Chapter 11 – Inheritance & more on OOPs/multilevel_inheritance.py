class Employee:
    a = 10

class Programmer(Employee):
    b = 20

class Manager(Programmer):
    c = 30

o = Employee()
print(o.a)

p = Programmer()
print(p.a)
print(p.b)

m = Manager()
print(m.a)
print(m.b)
print(m.c)