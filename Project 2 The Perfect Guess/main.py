import random
n = random.randint(1,100)
a = -1
gussess = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        gussess += 1
    elif(a<n):
        print("Higher number please")
        gussess += 1


print(f"You have guessed the number {n} correctly in {gussess} attempts")