class BankAccount:
    bank_name = "Banana Bank"
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return(self)

    def withdraw(self, amount):
        self.balance -= amount
        return(self)

    def display_account_info(self):
        print(f"balance : {self.balance}")

    def yield_interest(self):
        self.balance += (self.int_rate * self.balance)
        return(self)

accntone = BankAccount(0.05, 0)
accnttwo = BankAccount(0.05, 0)
accntone.deposit(200).deposit(100).deposit(150).withdraw(80).yield_interest().display_account_info(self)
accnttwo.deposit(150).deposit(150).withdraw(25).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info(self)
