class BankAccount:
    balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: {self.balance}")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
        
    def display_account_info(self):
        return f"Interest: {self.int_rate}, Balance: {self.balance}"
        

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.balance)
        return self

# checkings = BankAccount(0.05, 500)
# savings = BankAccount(0.02, 2500)

class User:

    def __init__(self, name):
        self.name = name
        self.account1 = BankAccount(int_rate=0.02, balance=0)
        self.account2 = BankAccount(int_rate=0.05, balance=0)
        
    def make_deposit_to1(self, amount): #--->   we need to deposit to make withdrawals!
        self.account1.deposit(amount)

    def make_deposit_to2(self, amount): #--->   we need to deposit to make withdrawals!
        self.account2.deposit(amount)
        
    def make_withdrawl(self, amount):
        self.account1.withdraw(amount)

    def make_withdraw2(self, amount):
        self.account2.withdraw(amount)
            
    def display_user_balance(self):
        print(f"User: {self.name}, Account1: {self.account1.display_account_info()}, Account2: {self.account2.display_account_info()}")

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.amount += amount
        self.display_user_balance()
        other_user.display_user_balance()
    


mina = User("Mina17")
jon = User("Jon13")
jack = User("Jack56")



#SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which 
# account they are withdrawing or depositing to

mina.make_deposit_to2(45)
mina.display_user_balance() #--->output: User: Mina17, Account1: Interest: 0.02, Balance: 0, Account2: Interest: 0.05, Balance: 45

