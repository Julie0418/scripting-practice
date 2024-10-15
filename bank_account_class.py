class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance =+ amount
            print(f"${amount} deposited")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn")
            else:
                print("insufficient Balance")
        else:
            print("Withdraw must be positive")

    def display_balance(self):
        print(f"your balance is: ${self.balance}")


account = BankAccount("Alice")

account.deposit(1000)   # Deposit $1000
account.withdraw(300)   # Withdraw $300
account.withdraw(200)   # Try to withdraw $800 (should fail due to insufficient funds)
account.display_balance() 