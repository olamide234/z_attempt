"""A Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
 These objects should allow for
1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories"""

class Budget:
    
    def __init__(self, category, new_balance=0):
        self.category, self.new_balance = category, new_balance

    def deposit(self):
        todeposit =  int(input('How much will you like to deposit for %s \n' % self.category))
        self.new_balance += todeposit #Budget.balance

    def withraw(self):
        towithdraw = int(input('How much will you like to withdraw from %s budget \n' % self.category))
        self.new_balance -= towithdraw

    def transfer(self):
        totransfer= int(input('How much will you like to transfer from %s budget \n' % self.category))
        self.new_balance -= totransfer
        return totransfer

    def check_balance(self):
        return ('Your balance for %s is: %d' % (self.category, self.new_balance))

category1 = Budget('Food')
category2 = Budget('Clothing')
print(category1.category)
# print(category1.new_balance)
category1.deposit()
category1.withraw()
bal = category1.check_balance()
print(bal)

category2.new_balance = category1.transfer()
print("Category1: balance for %s is %d" % (category1.category, category1.new_balance))
print("Category2: balance for %s is %d" % (category2.category, category2.new_balance))

print(category2.new_balance)
# category2.withraw()
category2.deposit()
bal2 = category2.check_balance()
print(bal2)
