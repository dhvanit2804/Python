'Write a function that takes a list and returns a new list with only even numbers'

def filter_even(num):
    even_num = [n for n in num if n % 2 == 0]
    return even_num

print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))