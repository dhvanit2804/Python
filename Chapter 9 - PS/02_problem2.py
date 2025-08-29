'''The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file 'Hi-score.txt' which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score. '''
import random

def game():
    print("You are playing a game")
    score = random.randint(1, 62)   # generates a random score between 1 and 62
    
    # Fetch the hiscore
    with open("hiscore.txt") as f:   # opens the file in read mode
        hiscore = f.read()           # reads the content of the file (as a string)
        if (hiscore != ""):          # if file is not empty
            hiscore = int(hiscore)   # convert it into integer
        else:
            hiscore = 0              # if empty, set hiscore = 0
    
    print(f"Your score {score}")
    
    # check if the new score is greater than the old high score
    if(score > hiscore):
        with open("hiscore.txt", "w") as f:  # open file in write mode
            f.write(str(score))              # save the new high score
    
    return score

game()
