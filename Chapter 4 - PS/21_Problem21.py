'Find the second largest number in a list.'

l = [10, 20, 30, 40, 50]
unique_l = list(set(l))
unique_l.sort()
print(unique_l[-2])