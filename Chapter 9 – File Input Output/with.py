# f = open("file.txt")
# print(f.read())
# f.close()

'The same can be written using with statement like this: '

with open("file.txt") as f:
    print(f.read())

'Here, we dont need to explicitly close the file. It will be closed automatically when the with block is exited.'