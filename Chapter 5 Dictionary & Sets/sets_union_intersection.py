'''s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
s.intersection({8,11}): Return a set which contains only item in both sets  {8}.'''

s1 = {28, 45, 44, 1}
s2 = {3, 28, 4, 12}

print(s1.union(s2)) # Return both sets combined but without duplicates
print(s1.intersection(s2)) # Return only the items that are in both sets