'Write a function to calculate the number of uppercase and lowercase letters in a string.'

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

print(count_case("Hello World"))