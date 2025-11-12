'What is Exception Handling in Python ?'
'# Exception Handling in Python is a mechanism to handle runtime errors.'
'# It allows the program to continue execution even after an error has occurred.'

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)

print("Program Continues...")