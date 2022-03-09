class BankAccount:
    balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance= self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
        
    def display_account_info(self):
        print(f"Interest: {self.int_rate}, Balance: {self.balance}")
        

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self



checkings = BankAccount(0.05, 500)
savings = BankAccount(0.02, 2500)

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display 
# the account's info all in one line of code (i.e. chaining)

# checkings.deposit(100).deposit(500).deposit(200).withdraw(600)
# print(checkings.balance) #--->output: 700

# checkings.yield_interest()
# print(checkings.balance) #----> output: 735 

# checkings.display_account_info() #---> output: Interest: 0.05, Balance: 735.0


#To the second account, make 2 deposits and 4 withdrawals, then yield interest
#  and display the account's info all in one line of code (i.e. chaining)

savings.deposit(500).deposit(600).withdraw(300).withdraw(200).withdraw(100).withdraw(100).yield_interest()
print(savings.balance) #---> output: 2958.0 YEEEY! IT WORKS NOW BC OF INDENTATION






#PLAYING!
# print(savings.int_rate) #--> output: 0.02
# print(checkings.balance) #---> output: 500

# checkings.deposit(300)
# print(checkings.balance) #---> output: 800

# checkings.withdraw(400)
# print(checkings.balance) #---> output: 400

# checkings.withdraw(500)
# print(checkings.balance) #---> output: Insufficient funds: Charging a $5 fee
#                                         # 395 (it charged a fee of 5 to my balance)

# checkings.withdraw(395)
# print(checkings.balance) # ---> output: 0 

# checkings.deposit(2500)
# print(checkings.balance) #---> output: 2500

# checkings.yield_interest(0.05)
# print(checkings.balance) # ---> output: 2625.0

# checkings.yield_interest(0.09)
# print(checkings.balance) # ----> output: 2861.25