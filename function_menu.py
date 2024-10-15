def display_menu():
    print("menu: ")
    print("1. convert string to uppercase")
    print("2. convert string to lower case")
    print("3. Exit")

def convert_to_upper():
    user_input = input("Enter any string: ")
    print(f"{user_input.upper()}: in uppercase")

def convert_to_lower():
    user_input = input("Enter any string: ")
    print(f"{user_input.lower()}: in lowercase")

def main():
    running = True

    while running:
        display_menu()
        choice = input("choose an option (1,2,3): ")

        if choice == '1':
            convert_to_upper()
        elif choice == '2':
            convert_to_lower()
        elif choice == '3':
            print("Exiting the program!")
            running = False
        else:
            print("incorrect choice! Try again!")
