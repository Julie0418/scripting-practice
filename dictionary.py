'''
Author: Julekha Khatoon
Date: 10/10/2024
Dscription: crate student dictionary and assign unique student id
'''

students = ["Alice", "Bob", "Charlie", "David", "Eve"]

student_ids ={}

student_id = 101

for student in students:
    student_ids[student] = student_id
    student_id += 1

print(student_ids)
