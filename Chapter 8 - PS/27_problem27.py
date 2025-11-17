'Write a function that accepts a list and returns another list containing only unique elements.'

def unique(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

print(unique([1, 2, 2, 3, 4, 4, 5]))