'This will return a list of lines from the file'
'''MODES OF OPENING A FILE 
r = open for reading 
w = open for writing  
a = open for appending 
+ = open for updating. 
rb will open for read in binary mode. 
rt will open for read in text mode. '''

f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

line2 = f.readline()
print(line2, type(line2))

line = f.readlines()
while (line != ""):
    print(line)
    line = f.readline()

f.close()