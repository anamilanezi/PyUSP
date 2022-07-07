# Write a program that converts the students scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    grade = ""
    if (student_scores[student] >= 91) and (student_scores[student] <= 100):
        grade = "Outstanding"
    elif (student_scores[student] >= 81):
        grade = "Exceeds Expectations"
    elif (student_scores[student] >= 71):
        grade = "Acceptable"
    elif (student_scores[student] <= 70):
        grade = "Fail"
    
    student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades) 