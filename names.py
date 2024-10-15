'''
Author: Julekha Khatoon
Date: 10/10/2024
Dscription: take name from user and provide length of the name, name in upper case, 
name in lower case and first letter of the name
'''

user_name = str(input("please enter your name: "))

print(f"Length of the the name is: {len(user_name)}")

print(f"Name in uppercase is: {user_name.upper()}")

print(f"name in lowercase is: {user_name.lower()}")

print(f"first letter of the name is: {user_name[0]}")

