class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    # Method to borrow the book
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")
    
    # Method to return the book
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")
    
    # Method to display book info
    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

# Create instances of the Book class
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Borrow and return books
book1.display_info()
book1.borrow()          # Borrow '1984'
book1.display_info()     # Display status after borrowing

book2.display_info()
book2.borrow()          # Borrow 'To Kill a Mockingbird'
book2.borrow()          # Try to borrow again (should print an error)
book2.return_book()     # Return 'To Kill a Mockingbird'
book2.display_info()     # Display status after returning