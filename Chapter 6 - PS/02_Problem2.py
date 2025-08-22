'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''

Student = "Dhvanit"

marks1 = int(input("Enter Marks 1 : "))
marks2 = int(input("Enter Marks 2 : "))
marks3 = int(input("Enter Marks 3 : "))

total = (100*(marks1 + marks2 + marks3))/300

if(total>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print(f"Student Name is {Student}")
    print("Congratulations You Are Pass...")
    print(f"Your Total Percentage is {total}")
else:
    print(f"Student Name is {Student}")
    print("You Are Failed, try again next year")
    print(f"Your Total Percentage is {total}")