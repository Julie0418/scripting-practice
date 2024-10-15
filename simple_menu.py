
running = True

while running:
    print("menu: ")
    print("1. convert string to uppercase")
    print("2. convert string to lower case")
    print("3. Exit")

    user_input = input("Enter your choice (1,2,3): ")
    if user_input == '1':
        string_input = input("Enter a string: ")
        print(f"{string_input.upper()} in uppercase")
    elif user_input == '2':
        string_input = input("Enter a string: ")
        print(f"{string_input.lower()} in lowercase")
    elif user_input == '3':
        print("exiting menu")
        running = False
    else:
        print("Enter valid menu option")



