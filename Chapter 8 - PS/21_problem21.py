'Write a function to reverse a list without using reverse().'

def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst = [item] + reversed_lst
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))