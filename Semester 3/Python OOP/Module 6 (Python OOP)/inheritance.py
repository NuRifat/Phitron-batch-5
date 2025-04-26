#Inheritance - is a fundamental concept that allows a class (called a child or derived class) to acquire properties and behaviors (fields and methods) from another class (called a parent or base class). Actually when we need common things to use then inheritance works

# Base class or Common Class
class Common_gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    def run(self):
        return f'Running the device: {self.brand}'
    def __repr__(self):
        return f'Running the device: {self.brand}, color: {self.color}, contry: {self.origin}'

# Child class inheriting from Common_gadget    
class Laptop(Common_gadget):
    def __init__(self, brand, price, color, origin, ssd):
        self.ssd = ssd
        super().__init__(brand, price, color, origin)
    def __repr__(self):
        print(super().__repr__())
        return f'{self.brand} has a ssd of {self.ssd}GB and the price is {self.price}'
    
class Phone(Common_gadget):
    def __init__(self, brand, price, color, origin,memory):
        self.memory = memory
        super().__init__(brand, price, color, origin)
    def __repr__(self):
        print(f'This is {self.brand} mobile, it is memory is {self.memory}GB')
        return super().__repr__()
    
print('\n------------LAPTOP---------------')
ipad = Laptop('iPad',45000,'Red','China',32)
print(ipad)
print(ipad.run())

print('\n------------PHONE---------------')
iphone = Phone('iPhone',120000,'Blue','US',128)
print(iphone)
print(iphone.run())