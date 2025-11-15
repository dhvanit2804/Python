'Count the frequency of each character in a string using a dictionary.'

string = input("Enter a string: ")

freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")
for key, value in freq.items():
    print(f"{key}: {value}")