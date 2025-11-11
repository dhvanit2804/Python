'''Convert a tuple of tuples into a flat tuple.
Example: ((1,2), (3,4)) → (1,2,3,4)'''

t = ((1,2),(3,4))
flat = tuple(i for sub in t for i in sub)
print(flat)
