a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swapping")
print("Value of a is", a)
print("Value of b is", b)

a, b = b, a
print("After swapping")
print("Value of a is", a)
print("Value of b is", b)