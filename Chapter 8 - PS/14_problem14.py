'Write a function that takes a list of numbers and returns the largest number.'

def largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(largest_number([3, 5, 1, 8, 2]))