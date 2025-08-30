'Add a static method in problem 2, to greet the user with hello.'

class Calculator:

    def square(self, num):
        self.num = num
        return num * num
    
    def cube(self, num):
        self.num = num
        return num * num * num
    
    def root(self, num):
        self.num = num
        return num ** 0.5

    @staticmethod
    def greet():
        print("Hello there")

c = Calculator()

c.greet()
print(c.square(4))
print(c.cube(4))
print(c.root(4))