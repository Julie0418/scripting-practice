'''
Author: Julekha Khatoon
Date: 10/10/2024
Dscription: calculate the number of contact and print phone number and email of john doe
'''
import rough_work

contacts = [
    ("John Doe", "555-1234", "john@example.com"),
    ("Jane Smith", "555-5678", "jane@example.com"),
    ("Bob Johnson", "555-9876", "bob@example.com")
]

print(f"the number of contact in the list is: {len(contacts)}")

for person in contacts:
    if person[0] == "John Doe":
        print(f"phone number of John doe is: {person[1]} and email is: {person[2]}")


