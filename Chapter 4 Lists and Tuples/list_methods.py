# l1 = [1,8,7,2,21,15] 
# • l1.sort(): updates the list to [1,2,7,8,15,21] 
# • l1.reverse(): updates the list to [15,21,2,7,8,1] 
# • l1.append(8): adds 8 at the end of the list  
# • l1.insert(3,8): This will add 8 at 3 index 
# • l1.pop(2): Will delete element at index 2 and return its value. 
# • l1.remove(21): Will remove 21 from the list.  

friends = ["Apple", "Banana", "Orange", 5, 345.06, False, "Sahil", "Gargi"]

print(friends)
friends.append("Dhvanit")
print(friends)
# friends.reverse() # Reverse The List
# print(friends)

l1 = [1, 34, 28, 4, 3, 11]
# l1.sort() # Upadate the List to incresing Order
l1.insert(3, 17) # # Insert 17 such that its index in the list is 3
value = l1.pop(1) # Detele Element at asigning Index and return its value.
print(value)
print(l1)
l1.remove(11) # Remove 11 from the list.
print(l1)