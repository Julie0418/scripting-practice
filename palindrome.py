
def is_palindrome(value):
    value_str = str(value)
    if value_str == value_str[::-1]:
        return True
    else:
        return False

def main():

    user_input = ''

    while user_input.lower() != 'exit':
        
        user_input = input("Enter any string or number to check if it is palindrom or type exit to quit: ")

        if user_input.lower() == 'exit':
            print("Exiting the program!")
            return
            
        try:
            num = int(user_input)
            if is_palindrome(num):
                print("The number is palindrome")
            else:
                print("The number is not paplindrome")
        except ValueError:
            if is_palindrome(user_input):
                print("The string is palindrome")
            else:
                print("The string is not palindrome")
        
main()