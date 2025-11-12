'What is List Comprehension?'
'''List comprehension is a concise way to create lists in Python. It consists of brackets containing an expression followed by a for clause, 
and can also include optional if clauses to filter items.'''
'List Comprehension is an elegant way to create lists based on existing lists.'
'It is more compact and faster than normal functions and loops for creating lists.'

myList = [1, 2, 8, 9, 28]

# squaredList = []
# for item in myList:
#     squaredList.append(item * item)

# Using List Comprehension
squaredList = [i * i for i in myList]

print(squaredList)