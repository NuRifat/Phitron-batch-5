class Shop:
    cart = [] #this is a class attribute, Shared by all instances of the class.Changing the value from one instance affects all others
    """ def __init__(self,owner):
        self.owner=owner """
        
    def add_to_cart(self,item):
        self.cart.append(item)

rifat_shop = Shop()
rifat_shop.add_to_cart('watch')
rifat_shop.add_to_cart('phone')
rifat_shop.add_to_cart('shirt')
print(rifat_shop.cart)

nisho_shop = Shop()
nisho_shop.add_to_cart('perfume')
nisho_shop.add_to_cart('sunglass')
nisho_shop.add_to_cart('shoe')
print(nisho_shop.cart)

#To solve this problem we need 'instance attribute'
class Shop:
    
    def __init__(self,owner):
        self.owner=owner
        self.cart = []
        
    def add_to_cart(self,item):
        self.cart.append(item)

rifat_shop = Shop('Rifat')
rifat_shop.add_to_cart('watch')
rifat_shop.add_to_cart('phone')
rifat_shop.add_to_cart('shirt')
print(rifat_shop.cart)

nisho_shop = Shop('Nisho')
nisho_shop.add_to_cart('perfume')
nisho_shop.add_to_cart('sunglass')
nisho_shop.add_to_cart('shoe')
print(nisho_shop.cart)