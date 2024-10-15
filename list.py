'''
Author: Julekha Khatoon
Date: 10/10/2024
Dscription: ask user to add fruit to the list and remove it
'''
fruit = ["apple", "mango"]

print(f"your favorate fruits are: {fruit}")

new_fruit = str(input("what fruit would you like to add as favourite: "))
fruit.append(new_fruit)
print(f"updated fruit list is: {fruit}")

remove_fruit = str(input("which fruit would you like to remove: "))

if remove_fruit in fruit:
    fruit.remove(remove_fruit)
    print(f"removed fruit is: {remove_fruit} and new list is {fruit}")
else:
    print(f"fruit is not in the list to remove")

