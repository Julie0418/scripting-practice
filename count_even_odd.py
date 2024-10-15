'''
Author - Julekha Khatoon
Date: 10/13/2024
Description: ask user to input score and display thier grade
'''

num = input("enter a list of number seperated by space: ").split()

num = [int(number) for number in num]

even_count = 0
odd_count = 0

index = 0 

while index < len(num):
    if num[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    index += 1 

print(f"there are {even_count} even numbers")
print(f"there are {odd_count} odd numbers")