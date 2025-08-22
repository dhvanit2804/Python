# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
d = int(input("Enter D : "))

if(a>b and a>c and a>d):
    print(a)
    print("A is Greatest")

elif(b>a and b>c and b>d):
    print(b)
    print("B is Greatest")

elif(c>a and c>b and c>d):
    print(c)
    print("C is Greatest")
    
else:
    print(d)
    print("D is Greatest")