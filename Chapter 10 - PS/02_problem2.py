'Write a class “Calculator” capable of finding square, cube and square root of a number.'

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

c = Calculator()

print(c.square(4))
print(c.cube(4))
print(c.root(4))