'This will return a list of lines from the file'

f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

line = f.readlines()
while (line != ""):
    print(line)
    line = f.readline()

f.close()