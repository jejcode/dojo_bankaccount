class BankAccount:
    all_accounts = []
    def __init__(self, interest, balance = 0):
        self.interest = interest
        self.balance = balance
        print(f"Opening balance: {self.balance}")
        BankAccount.all_accounts.append(self)
    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -=  5
        else:
            self.balance -= amount            
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
        else:
            print('No interest payment due to non-positive balance.')
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for user in cls.all_accounts:
            print(f"Balance: {user.balance}")

user1 = BankAccount(.02,400)
user2 = BankAccount(.005)

user1.deposit(250).deposit(500).deposit(122).withdraw(400).yield_interest().display_account_info()
user2.deposit(75).deposit(75).withdraw(10).withdraw(25).withdraw(300).withdraw(15).yield_interest().display_account_info()

BankAccount.display_all_accounts()