# Write a program to show student grading system in Python.

print("Enter your marks obtained in 4 subjects: ")

english = int(input("English: "))

maths = int(input("Maths: "))

science = int(input("Science: "))

social = int(input("Social: "))

total_marks = english + maths + science + social

average = total_marks / 4

if (average >= 91) & (average <= 100):

    print("Grade A")

elif (average >= 81) & (average <= 90):

    print("Grade B")

elif (average >= 71) & (average <= 80):

    print("Grade C")

elif (average >= 61) & (average <= 70):

    print("Grade D")

elif (average >= 51) & (average <= 60):

    print("Grade E")

elif (average >= 0) & (average <= 50):

    print("Grade F")

else:

    print("Invalid Input")