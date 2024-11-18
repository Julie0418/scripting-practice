'''
Author: Julekha Khatoon
Date: 10/15/2024
Description: This program takes input for users in 3 departments and displays the number of users in each department and the remaining available users.
'''

num_department = 3
max_total_user = 32
total_user = 0

user_input = ''

while user_input.lower() != 'exit':
    
    user1_input = int(input("Enter the number of users in the first department: "))
    user2_input = int(input("Enter the number of users in the second department: "))
    user3_input = int(input("Enter the number of users in the third department: "))

    total_user = user1_input + user2_input + user3_input

    if total_user > max_total_user:
        print("You have exceeded the maximum allowable users.")
    elif total_user == max_total_user:
        print("There are no additional users allowed!")
    else:
        remaining_user = max_total_user - total_user
        print(f"There are {remaining_user} users still available.")

    
    print(f"Users in Department 1 is: {user1_input}")
    print(f"Users in Department 2 is: {user2_input}")
    print(f"Users in Department 3 is: {user3_input}")

    
    user_input = input("Type 'exit' to quit or press Enter to continue: ")
