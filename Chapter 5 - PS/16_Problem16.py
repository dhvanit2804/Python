'''Reverse key-value pairs of dictionary:
{"a":1, "b":2, "c":3} → {1:"a", 2:"b", 3:"c"}'''

d = {"a":1, "b":2, "c":3}

reversed_dict = {value: key for key, value in d.items()}
print(reversed_dict)