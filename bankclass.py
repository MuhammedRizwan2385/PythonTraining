#Implement a class for a Bank Account with deposit and withdrawal methods.
class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return self.balance
        else:
            return "Insufficient Balance"
acc=BankAccount(1000)
print(acc.deposit(500))
print(acc.withdraw(2000))
