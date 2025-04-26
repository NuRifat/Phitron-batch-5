class BankAccount:
    def __init__(self,name,balance):
        self.name = name #public attributes
        self.__balance = balance #private attributes

    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Insufficient funds')
    
    def check_balance(self):
        return self.__balance

rifat_acc = BankAccount('Rifat',10000)
print(rifat_acc.name)
#print(rifat_acc.__balance) #since it is private will be given error
print(rifat_acc.check_balance())
rifat_acc.withdraw(5000)
print(rifat_acc.check_balance())

#in public attributes we can change the value also but not possible for private
rifat_acc.name = 'Sabbir'
print(rifat_acc.name)

# Still accessible through name mangling (not recommended)
print(rifat_acc._BankAccount__balance)  # ⚠️ Not ideal, but possible