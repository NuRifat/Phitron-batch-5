class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount>0:
            self.balance += amount
            print(f'After deposit {amount}, your new balance is {self.balance}')
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'Sorry the amount is too low, you can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'The amount is too high. You can withdraw below {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'After withdraw your remaining amount is {self.get_balance()}')

print('------------CITY BANK-----------')
city = Bank(20000)
city.withdraw(50)
city.withdraw(500)
city.deposite(1000)

print('------------BRAC BANK-----------')
brac = Bank(1000)
brac.withdraw(200000)
brac.withdraw(500)
brac.deposite(200)