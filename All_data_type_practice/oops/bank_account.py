# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customer = {}

    def create_account(self, account_num, balance=0):
        if account_num in self.customer:
            print("This account number already exist")
        else:
            self.customer[account_num] = balance
            self.customer.update({account_num: balance})
            print("Account created successfully")
            print(self.customer)


account_num = 123456789
bank = Bank()
bank.create_account(account_num)
account_num1 = 123456789
bank2 = Bank()
bank2.create_account(account_num1)