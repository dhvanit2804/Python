'''Write a program to read the text from a given file 'poems.txt' and find out 
whether it contains the word 'twinkle'. '''

f = open("poems.txt")
content = f.read()

if("twinkle" in content):
    print("The word twinkle present in content")
else:
    print("The word twinkle is not present in content")

f.close()