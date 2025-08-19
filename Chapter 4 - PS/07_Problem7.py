# Take 5 numbers from the user and store them in a list. Print the maximum and minimum.

num = []

n1 = int(input("Enter Number: "))
num.append(n1)

n2 = int(input("Enter Number: "))
num.append(n2)

n3 = int(input("Enter Number: "))
num.append(n3)

n4 = int(input("Enter Number: "))
num.append(n4)

n5 = int(input("Enter Number: "))
num.append(n5)

print(max(num))
print(min(num))