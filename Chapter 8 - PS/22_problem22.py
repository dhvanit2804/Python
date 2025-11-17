'Write a function that takes a number and returns the sum of its digits.'

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

print(sum_of_digits(1234))