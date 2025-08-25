'''A function is a group of statements performing a specific task. 

When a program gets bigger in size and its complexity grows, it gets difficult for a 
program to keep track on which piece of code is doing what! 

A function can be reused by the programmer in a given program any number of '''

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))

# average = (a+b+c)/3
# print(average)

'''There are two types of functions in python: 

• Built in functions (Already present in python) 
• User defined functions (Defined by the user) 

Examples of built in functions includes len(), print(), range() etc.

The avg() function we defined is an example of user defined function. '''

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)

avg() # This is Called function Call