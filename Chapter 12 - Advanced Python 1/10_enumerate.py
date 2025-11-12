'What is Enumerate in python ?'
'The "enumerate" function adds counter to an iterable and returns it in a form of enumerating object.'

l = [45, 28, 3, 17, 235]

# index = 0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index += 1

# This can be simplified by using enumerate function

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")