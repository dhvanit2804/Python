'''What is a Class Method?

A class method is a method that is bound to the class, not the object.
It takes the class itself as the first argument, usually named cls (like self for objects).
You define it using the @classmethod decorator.'''

class Employee:
    a = 10
    @classmethod
    def show(cls):
        print(f"The class Value of a is {cls.a}")

b = Employee()
b.a = 20
b.show()