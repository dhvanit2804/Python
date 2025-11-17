'Write a function that accepts a dictionary and returns the key with the highest value.'

def key_with_highest_value(d):
    if not d:
        return None
    highest_key = max(d, key=d.get)
    return highest_key

print(key_with_highest_value({'a': 10, 'b': 20, 'c': 15}))