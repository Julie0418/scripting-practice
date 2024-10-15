'''
Author: Julekha Khatoon
Date: 10/10/2024
Dscription: calculate average age and average score of the students
'''

students = [
    ("Alice", 20, 95),
    ("Bob", 22, 88),
    ("Charlie", 21, 75),
    ("David", 19, 92),
    ("Eve", 23, 78)
]

total_age = 0
total_score = 0

for student in students:
    total_age += student[1]
    total_score += student[2]

avg_age = total_age / len(students)
avg_score = total_score / len(students)

print(f"the average age of the students is: {avg_age:.2f}")
print(f"the average scrore of the students is: {avg_score:.2f}")


      