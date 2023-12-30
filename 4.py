class Bank:
    def __init__(self):
        self.accounts = {}

    def createAccount(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account created successfully for account number {account_number}")
        else:
            print(f"Account with account number {account_number} already exists.")

    def checkBalance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Balance for account number {account_number}: ${balance}")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount} into account number {account_number}")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew ${amount} from account number {account_number}")
            else:
                print("Insufficient funds.")
        else:
            print(f"Account with account number {account_number} does not exist.")


bank = Bank()

bank.createAccount("12345", 1000)
bank.createAccount("67890")

bank.checkBalance("12345")
bank.checkBalance("67890")

bank.deposit("12345", 500)
bank.withdraw("67890", 200)

bank.checkBalance("12345")
bank.checkBalance("67890")
