from order import Order
from food_item import Food_item


class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def add_customer(self, restaurant, customer):
        restaurant.add_customer(customer)

    def remove_customer(self, restaurant, customer_name):
        restaurant.remove_customer(customer_name)

    def view_customer(self, restaurant):
        restaurant.view_customer()
    # manage restaurant menu

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def view_items(self, restaurant):
        restaurant.menu.show_menu()


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name)
        self.email = email
        self.address = address
        self.balance = None
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def view_balance(self):
        self.balance = 1000
        print(f'Your initial balance is {self.balance}Tk')

    def add_balance(self, amount):
        self.balance += amount
        print(f'{amount}Tk is added\nYour new blance is {self.balance}tk')

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Exccedded")
            else:
                customer_item = Food_item(item.name, item.price, quantity)
                self.cart.add_item(customer_item)
                item.quantity -= quantity
                print("Item added")
        else:
            print("Item not found")

    def view_cart(self):
        print('*******View Cart******')
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price: {self.cart.total_price}")

    def pay_bill(self):
        total_price = self.cart.total_price
        if total_price > self.balance:
            print(f"Sorry you do not have sufficient balance\nPlease add balance")
            return
        print(f"Total {total_price}tk paid successfully")
        self.balance -= total_price
        print(f"Your new balance is {self.balance}")
