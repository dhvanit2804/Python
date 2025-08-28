import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid choice! Please enter only 's', 'w', or 'g'.")
    exit()
    
you = youDict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")


if(computer == you):
     print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer ==0 and you == -1):
            print("You Win!")

    elif(computer == 0 and you == 1):
            print("You Lose!")

    else:
        print("Something went wrong!")