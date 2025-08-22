a = int(input("Enter Your age : "))

# If elif else ladder
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