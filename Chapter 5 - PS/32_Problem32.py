'Count how many vowels are present in a string using set.'

s = "Hello World"

vowels = {'a', 'e', 'i', 'o', 'u'}

count = 0
for char in s.lower():
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)