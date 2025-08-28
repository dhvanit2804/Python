'''
Recursion is a process in which a function calls itself directly or indirectly.
A recursive function must have a base case (a condition under which it stops calling itself)
and a recursive case (the part of the function that includes the self-call).
'''

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to find its factorial: "))
print(f"The Factorial of {n} is {factorial(n)}")