import os

# Function to check for files with zero size in a specified directory
def check_zero_size_files(directory):
    # List to store the names of files with zero size
    zero_size_files = []
    
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)  # Get full path of the file
        
        # Check if the file exists and is not a directory
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)  # Get the size of the file in bytes
            if file_size == 0:  # If the file size is zero, add it to the list
                zero_size_files.append(filename)
    
    return zero_size_files


# Main function to test the script
def main():
    # Get the directory path from the user
    directory_path = input("Enter the directory path to check for zero-sized files: ")
    
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print("Invalid directory path. Please try again.")
        return
    
    # Call the function to find zero-sized files
    zero_size_files = check_zero_size_files(directory_path)
    
    # Print the results
    if zero_size_files:
        print("Zero-sized files found:")
        for file in zero_size_files:
            print(f"- {file}")
    else:
        print("No zero-sized files found.")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
