'In this example, we demonstrate the use of try, except, and else blocks in Python.'
'else block executes only if no exceptions are raised in the try block.'
'This is executed only if the try was successful'

try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")