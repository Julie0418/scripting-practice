'''
Author: Julekha Khatoon
Date: 10/10/2024
Dscription: taking two number from user and performing operations
'''

# Get two number form user
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

#perform the operation
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

#handle division by zero
if second_number != 0:
    division = first_number / second_number
    integer_division = first_number // second_number
    modulus = first_number % second_number
else:
    division = "undefined (division by zero)"
    integer_division = "undefined (division by zero)"
    modulus = "undefined (division by zero)"

#display the result
print(f"Addition of the two number is: {addition}")
print(f"Subtraction of the two number is: {subtraction}")
print(f"multiplication of the two number is: {multiplication}")
print(f"division of the two number is: {division}")
print(f"Integer division of the two number is: {integer_division}")
print(f"Modulus of the two number is: {modulus}")


