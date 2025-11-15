'Write a program to find the key with the maximum value in a dictionary.'

data = {
    'a': 10,
    'b': 25,
    'c': 15
}

max_key = max(data, key=data.get)
print(f"The key with the maximum value is: {max_key} with value {data[max_key]}")