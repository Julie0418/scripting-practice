'''
Author - Julekha Khatoon
Date: 10/13/2024
Description: ask user to input score and display thier grade
'''

user_input = input("Enter a list of number seperated by spaces: ").split()

numbers = []

for num in user_input:
    try:
        number = int(num)
        if number < 0:
            print(f"{number} is a negative number, skipping this value")
        else:
            numbers.append(number)
    except ValueError:
        print(f"{num} is not a valid number, skipping this value")


if len(numbers) == 0:
    print("No valid number was entered")
else:
    total_sum = sum(numbers)
    
    if total_sum > 100:
        print(f"sum is {total_sum} and is greater than 100")
    elif total_sum == 100:
        print("sum id equal to 100")
    else:
        print("sum is less than 100")
