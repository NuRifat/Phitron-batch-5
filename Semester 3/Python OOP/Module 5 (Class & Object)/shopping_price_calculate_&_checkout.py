class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price']*item['quantity']
        print('Total price: ', total)
        if (total > amount):
            print(f'Please provide {total-amount}Tk more')
        else:
            print(f'Here is your item and extra more {amount-total}Tk')


rifat = Shopping('Rifat')
rifat.add_to_cart('Orange', 200, 50)
rifat.add_to_cart('Mango', 500, 20)
rifat.add_to_cart('Coconut', 50, 5)
rifat.add_to_cart('Guava', 100, 10)
print(rifat.cart)
rifat.checkout(25000)
