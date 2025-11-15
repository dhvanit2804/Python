'Create a nested dictionary for 3 students and display name & marks.'

students = {
    1: { 'name' : "Dhvanit", 'marks': 85 },
    2: { 'name' : "Rahul", 'marks': 90 },
    3: { 'name' : "Meet", 'marks': 78 }
}

print("Roll No:", 1)
print("Name :", students[1]['name'])
print("Marks:", students[1]['marks'])

print("\nRoll No:", 2)
print("Name :", students[2]['name'])
print("Marks:", students[2]['marks'])

print("\nRoll No:", 3)
print("Name :", students[3]['name'])
print("Marks:", students[3]['marks'])