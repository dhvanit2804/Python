'Write a program to find out the line number where python is present from ques 6.'

line = 1
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is present. Line no : {lineno}")
        break
    lineno += 1

else:
    print("python is not present")