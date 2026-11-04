# Implement deposits, withdrawals, balance checks, and validation against invalid transactions.Implement deposits, withdrawals, balance checks, and validation against invalid transactions.

class BankAccount:
    def __init__(self, balance = 1000, ):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

account1 = BankAccount(500)
account1.deposit(600)
account1.withdraw(300)
print(account1.check_balance())