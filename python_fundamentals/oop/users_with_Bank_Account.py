class BankAccount:
    bank_name = "RoseBud Bank"

    def __init__(self, int_rate = 0.05, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return(self)

    def withdrawal(self, amount):
        self.balance -= amount
        return(self)

    def display_account_info(self):
        print(f"balance : {self.balance}")

    def yield_interest(self):
        self.balance += (self.int_rate * self.balance)
        return(self)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate=0.05, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self
    
    def display_user_balance(self):
        print(f"balance : {self.account.balance}")

johnny = User ("Johnny Rose","jrose@schittsscreek.com") 
moira = User("Moira Rose", "mrose@schittsscreek.com")

johnny.make_deposit(200).make_deposit(100).make_deposit(150).make_withdrawal(80).display_user_balance()
moira.make_deposit(150).make_deposit(150).make_withdrawal(25).make_withdrawal(20).display_user_balance()

