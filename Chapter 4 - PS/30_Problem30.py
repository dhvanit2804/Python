'Replace an element in a tuple.'

t = (1, 2, 3, 4, 5)
t1 = list(t)

t1[2] = 10

t2 = tuple(t1)
print(t2)