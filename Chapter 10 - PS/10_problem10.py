'Write a class BankAccount with methods deposit and withdraw.'

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.amount = amount
        if self.amount > 0:
            self.balance += amount
        else:
            print("Please fill Validate Amount...")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Please fill Validate Amount...")
    
    def showAccountdetails(self):
        print(f"The Account Holder Name is {self.name}")
        print(f"The Current Balance of account is {self.balance}")

d = BankAccount("Dhvanit", 100000)

d.showAccountdetails()
d.withdraw(10000)
d.showAccountdetails()
d.deposite(20000)
d.showAccountdetails()