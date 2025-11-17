'''Write a program to group students by marks:

Input: {"A":90, "B":80, "C":90, "D":70}
Output: {90:["A","C"], 80:["B"], 70:["D"]}'''

students = {"A":90, "B":80, "C":90, "D":70}
grouped_students = {}
for name, marks in students.items():
    if marks not in grouped_students:
        grouped_students[marks] = []
    grouped_students[marks].append(name)
print(grouped_students)