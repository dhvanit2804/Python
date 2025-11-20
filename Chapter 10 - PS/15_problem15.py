'Make a class Calculator with static methods for add, sub, mul, div.'

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
# Example usage:
print("Addition: ", Calculator.add(10, 5))     
print("Subtraction: ", Calculator.sub(10, 5))
print("Multiplication: ", Calculator.mul(10, 5))  
print("Division: ", Calculator.div(10, 5))        