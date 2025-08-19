# a = (1, 7, 2) 
# a.count (1): a count (1) will return number of times 1 occurs in a. 
# a.index (1) will return the index of first occurrence of 1 in a.
# len(tuple) → Returns the number of items.
# max(tuple) → Returns the largest element.
# min(tuple) → Returns the smallest element.
# sum(tuple) → Returns the sum of elements (only if numbers).
# sorted(tuple) → Returns a sorted list from the tuple.
# tuple(iterable) → Converts an iterable into a tuple.

a = (1,45,45,3424)
print(a)

num = a.count(45)
print(num)

print(sum(a)) # Sum to interger in tuple
print(max(a)) # Returns Large value in tuple.
print(min(a)) # Returns small value in tuple.
print(len(a)) # Returns length Of tuple.
print(sorted(a)) # Returns a tuple in assending Order.
b = a.index(3424)
print(b) # Returns a index of value.

print(45 in a) # Checks the Value in tuple and returns a boolen value.

repeated = a * 3 # Returns tuple in mutliplication value
print(repeated)

# Tuple Unpacking
# Tuple unpacking means assigning values from a tuple to multiple variables in a single step.
my_tuple = [10, 20, 30]
a, b, c = my_tuple
print(a,b,c)