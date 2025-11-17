'''Count digits in a number
Input a number and count how many digits it has.
Example: 5649 → 4 digits'''

num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10
    count += 1

print(f"Number of digits: {count}")