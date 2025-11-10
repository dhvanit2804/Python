import random
n = random.randint(1,100)
a = -1
gussess =0
while(a != n):
    gussess += 1
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")

print(f"You have guessed the number {n} correctly in {gussess} attempts")