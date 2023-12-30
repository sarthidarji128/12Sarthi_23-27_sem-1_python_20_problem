from datetime import datetime

class Transaction:

    def verify_pin(account, entered_pin):
        return account.pin == entered_pin

    def record_transaction(account, transaction_type, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction_record = {"timestamp": timestamp, "type": transaction_type, "amount": amount}
        account.transactions.append(transaction_record)

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            Transaction.record_transaction(self, "Withdrawal", amount)
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            Transaction.record_transaction(self, "Deposit", amount)
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def transfer_funds(self, target_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            Transaction.record_transaction(self, f"Transfer (To: {target_account.account_number})", amount)
            Transaction.record_transaction(target_account, f"Transfer (From: {self.account_number})", amount)
            return f"Funds transfer of ${amount} to {target_account.account_number} successful. New balance: ${self.balance}"
        else:
            return "Invalid transfer amount or insufficient funds."

    def display_transactions(self):
        print(f"Transaction History for Account {self.account_number}: ")
        for transaction in self.transactions:
            print(
                f"{transaction['timestamp']} - {transaction['type']}: ${transaction['amount']}"
            )

class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account


account1 = Account(account_number="123456", pin="1234", balance=1000)
account2 = Account(account_number="789012", pin="5678", balance=500)

user1 = User(name="u1", account=account1)
user2 = User(name="u2", account=account2)

while True:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == "exit":
        exit()

    if Transaction.verify_pin(account1, entered_pin):
        print(f"Hello, User!")
        print("PIN verified. Welcome to the ATM.")

        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Transfer Funds")
            print("5. Display Transaction History")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                print(f"Your account balance: ${user1.account.check_balance()}")

            elif choice == "2":
                withdrawal_amount = float(input("Enter the withdrawal amount: $"))
                withdrawal_result = user1.account.withdraw_cash(withdrawal_amount)
                print(withdrawal_result)

            elif choice == "3":
                deposit_amount = float(input("Enter the deposit amount: $"))
                deposit_result = user1.account.deposit_cash(deposit_amount)
                print(deposit_result)

            elif choice == "4":
                target_account_number = input("Enter the target account number for transfer: ")
                target_account = user2.account if target_account_number == user2.account.account_number else None
                if target_account:
                    transfer_amount = float(input("Enter the transfer amount: $"))
                    transfer_result = user1.account.transfer_funds(target_account, transfer_amount)
                    print(transfer_result)
                else:
                    print("Invalid target account number.")

            elif choice == "5":
                user1.account.display_transactions()

            elif choice == "6":
                print("Exiting ATM. Have a great day!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
    
    else:
        print("Invalid PIN! \nPlease enter PIN again")
