""" Multilevel Inheritance is a type of inheritance where a class is derived from a class that is already derived from another class.
It creates a chain of inheritance — like a family tree with grandparent → parent → child. """

#parent class
class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'This is {self.name} , its price is {self.price}'

# Child class inheriting from Vehicle  
class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat = seat
        # Call parent constructor to set name and price
        super().__init__(name, price)

    def __repr__(self):
        print(f'{self.name} bus has total {self.seat} seats')
        return super().__repr__()

# Grandchild class inheriting from Bus
class AC_bus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self):
        print(super().__repr__())
        return f'This bus teperature is {self.temperature}'
    
greenline = AC_bus('Green Line',2000,60,15)
print(greenline)