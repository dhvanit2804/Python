# add(x) → Adds an element x to the set.
# remove(x) → Removes element x, raises error if not present.
# discard(x) → Removes element x, does nothing if not found.
# pop() → Removes and returns a random element from the set.
# clear() → Removes all elements (makes set empty).

'''PROPERTIES OF SETS 
1. Sets are unordered => Element`s order doesn`t matter 
2. Sets are unindexed => Cannot access elements by index 
3. There is no way to change items in sets. 
4. Sets cannot contain duplicate values. '''

s = {1, 5, 32, 54,5, 5, 5, "Dhvanit"}
print(s, type(s))

s.add(566)
print(s, type(s))

s.remove(1)
print(s)