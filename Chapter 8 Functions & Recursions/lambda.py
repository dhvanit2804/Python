def add(x, y):
    return x + y

print(add(2, 3))

'What is a lambda function?'
'A lambda function is a small anonymous function that can take any number of arguments but can only have one expression.'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)