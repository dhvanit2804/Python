'''What are Property Decorators?

In Python, property decorators (@property, @<property>.setter, @<property>.deleter) are special decorators used to create managed attributes.
They allow you to define getter, setter, and deleter methods in a clean way, while still accessing attributes using dot (.) notation.'''

class Employee:
    a = 10
    @classmethod
    def show(cls):
        print(f"The class Value of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

b = Employee()
b.a = 20
b.name = "Dhvanit Parate"
print(b.name)
print(b.fname)
print(b.lname)

b.show()