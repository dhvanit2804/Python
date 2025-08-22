a = int(input("Enter Your age : "))

# IF Statement 1
if(a%2==0):
    print("a is even")

# If elif else 2
if(a>=18):
    print("You Are above the age of consent")
    print("Good for you")
    
elif(a<0):
    print("You Are entering an negative age")

elif(a==0):
    print("You Are entering 0 Which is not a valid age")

else:
    print("You Are below the age of coscent")

print("End Of Program...")