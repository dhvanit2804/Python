# a.items(): Returns a list of (key,value)tuples. 
# a.keys(): Returns a list containing dictionary's keys. 
# a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
# a.get("name"): Returns the value of the specified keys (and value is returned eg."harry" is returned here). 

marks = {
    "Dhvanit": 99,
    "Meet": 65,
    "Rohan": 23,
    "list": [1,2,3],
    0 : "DHVANIT"
}

print(marks.items()) # Print Keys and Values.
print(marks.keys()) # Print Keys.
print(marks.values()) # Print Values.

# In This Update Method if the key already exists, it will update the value of that key and
# if the key does not exist, it will add the key-value pair to the dictionary.
marks.update({"Dhvanit": 98, "Jainish": 77}) # UPDATE DICTIONARY VALUE
print(marks)

print(marks.get("Dhvanit"))
print(marks.get("Dhvanit1")) # Prints None
print(marks["Dhvanit1"]) # Returns a Error

# OUTPUT
# dict_items([('Dhvanit', 99), ('Meet', 65), ('Rohan', 23), ('list', [1, 2, 3]), (0, 'DHVANIT')])
# dict_keys(['Dhvanit', 'Meet', 'Rohan', 'list', 0])
# dict_values([99, 65, 23, [1, 2, 3], 'DHVANIT'])
# {'Dhvanit': 98, 'Meet': 65, 'Rohan': 23, 'list': [1, 2, 3], 0: 'DHVANIT', 'Jainish': 77}
# 98