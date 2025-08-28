'''
The random-access memory is volatile, and all its contents are lost once a program 
terminates. In order to persist the data forever, we use files. 

A file is data stored in a storage device. A python program can talk to the file by reading 
content from it and writing content to it.
'''
'''
TYPE OF FILES. 
There are 2 types of files: 
1. Text files (.txt, .c, etc) 
2. Binary files (.jpg, .dat, etc) 
'''

'''
Modes:
"r" → read (default)
"w" → write (overwrites file if it exists)
"a" → append (adds new data without deleting old data)
"b" → binary mode (for images, videos, etc.)
"x" → create new file, error if exists
'''

f = open("file.txt")
data = f.read()
print(data)
f.close()