'''Input 2 sets from user and print:
union
intersection
difference
symmetric difference'''

set1 = set(map(int, input("Enter elements of set 1 separated by space: ").split()))
set2 = set(map(int, input("Enter elements of set 2 separated by space: ").split()))

print("\n------ RESULTS ------")

print(f"Union: {set.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")
print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")