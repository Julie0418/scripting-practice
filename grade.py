'''
Author - Julekha Khatoon
Date: 10/13/2024
Description: ask user to input score and display thier grade
'''

score = float(input("Enter you Score: "))

if (score < 0 or score > 100):
    print("Score cannot be more than 100 or less than 0, Try agian.")
elif (score >= 90 and score <= 100):
    print("your grade is A ")
elif(score >= 80 and score < 90):
    print("your grade is B ")
elif(score >= 70 and score < 80):
    print("your grade is C ")
elif(score >= 60 and score < 70):
    print("your grade is D ")
else:
    print("your grade is F ")

