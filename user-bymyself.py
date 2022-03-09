# 1 Create a class 

class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0 
        

    def make_deposit(self, amount): #--->   we need to deposit to make withdrawals!
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        self.display_user_balance()
        other_user.display_user_balance()

mina = User("Mina17")
jon = User("Jon13")
jack = User("Jack56")

#DEPOSITS

mina.make_deposit(500)
print(mina.amount) #output: 500
mina.make_deposit(200)
print(mina.amount) #output : 700
jon.make_deposit(500) #---> We are gonna transfer 200 to Jon.
print(jon.amount)

#WITHDRAWALS

mina.make_withdrawl(300)
print(mina.amount) #output: 400
mina.make_withdrawl(100)
print(mina.amount) #output: 300

#USER BALANCE 

mina.display_user_balance() #output: User:Mina, Balance:300

#BONUS

mina.transfer_money(jon, 200)
print(jon.amount)
print(mina.amount) #--->output: User: Mina17, Balance: 300
    #                                 User: Mina17, Balance: 100
    #                                 User: Jon13, Balance: 700
    #                                 700
    #                                 100