'Write a program to find elements present in tuple1 but not in tuple2.'

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

result = tuple(item for item in t1 if item not in t2)
print(f"Elements in tuple1 but not in tuple2: {result}")