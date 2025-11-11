'Find the index of all occurrences of a value in a tuple.'
t = (1, 2, 3, 2, 4, 2, 5)
value_to_find = 2
indices = [index for index, value in enumerate(t) if value == value_to_find]
print(f"Indices of occurrences of {value_to_find} in tuple: {indices}")