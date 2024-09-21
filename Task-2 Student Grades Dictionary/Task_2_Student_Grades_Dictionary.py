#Course: CIS 103
#Instructor: Md Ali
#Student: Sahar Iqbal
#Date: 09/20/2024

# Task: 02 Student Grades Dictionary:

# Create a dictionary with Student_grades:
Student_grades = {"Alice": 85, "Bob": 92, "Charlie": 87, "Diana": 78}
print(Student_grades)

# Add a new student, 'Edward' , with a grade of 90
Student_grades["Edward"] = 90
print("After Adding 'Edward':", Student_grades)

# Update 'Bob's' grades to 95
Student_grades["Bob"] = 95
print("After Updating Bob's grade:", Student_grades)

# Remove 'Diana' from the dictionary (she dropped the course)
del Student_grades['Diana']
print("After removing Diana:", Student_grades)

# Calculate the average grade of all remaining students
total_grades = sum(Student_grades.values())
num_students = len(Student_grades)
average_grade = total_grades / num_students 

# Print the average grade
print("Average grade of all students:", average_grade)

# Challenge: Find and print the name of the student with the highest grade
highest_grade_student = max(Student_grades, key=Student_grades.get)
highest_grade = Student_grades[highest_grade_student]

# Print the student with the highest grade
print("Student with the highest grade:", highest_grade_student, "with a grade of", highest_grade)







