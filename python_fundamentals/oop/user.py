
class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.account
    
    def make_deposit(self, amount):
        self.amount += amount
        return(self)

    def make_withdrawal(self, amount):
        self.balance -= amount
        return(self)
    
    def display_user_balance(self):
        print(f"balance : {self.balance}")

account1 = User
account2 = User
account3 = User

account1.make_deposit(100).make_deposit(50).make_deposit(500).make_withdrawal(75)
account2.make_deposit(50).make_deposit(1150).make_withdrawal(50).make_withdrawal(200)
account3.make_deposit(2000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200)
print(self.balance())