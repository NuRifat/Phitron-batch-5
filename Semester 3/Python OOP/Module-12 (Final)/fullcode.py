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


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.menu = Menu()

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer is added")

    def remove_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                self.customers.remove(customer)
                print(f"Customer - {customer_name} is removed")
                return
        print("No customer available with this name")

    def view_customer(self):
        print('__________Customer List:___________')
        print("Name\tEmail\tAddress")
        for cstm in self.customers:
            print(f"{cstm.name}\t{cstm.email}\t{cstm.address}")


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"item - {item.name} is added")

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'Item - {item.name} is deleted')
        else:
            print("Item not found")

    def show_menu(self):
        print("********MENU********")
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')


class Food_item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Order():
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price*quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}


rifater_res = Restaurant("Rifat's Restaurant")


def admin_menu():
    name = input("Enter Admin Name: ")
    admin = Admin(name)
    while True:
        print(f"\n Welcome Admin {admin.name}\n")
        print("--- Admin Menu ---")
        print("1. Create Customer Account")
        print("2. Remove Customer Account")
        print("3. View all Customers")
        print("4. Manage Restaurant Menu")
        print("5. Exit")

        option = int(input("Enter an option: "))

        if option == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            customer = Customer(name=name, email=email, address=address)
            admin.add_customer(rifater_res, customer=customer)

        elif option == 2:
            name = input("Enter name: ")
            admin.remove_customer(rifater_res, name)
        elif option == 3:
            admin.view_customer(rifater_res)
        elif option == 4:
            while True:
                print("*****MENU MANAGEMENT*****")
                print("1. Add Menu")
                print("2. Remove Menu")
                print("3. View Menu")
                print("4. Exit")

                option = int(input("Enter an option: "))
                if option == 1:
                    name = input("Enter item name: ")
                    price = int(input("Enter item price: "))
                    quantity = int(input("Enter item quantity: "))
                    item = Food_item(name=name, price=price, quantity=quantity)
                    admin.add_new_item(rifater_res, item)
                elif option == 2:
                    item_name = input("Enter the item name to delete: ")
                    admin.remove_item(rifater_res, item_name)
                elif option == 3:
                    admin.view_items(rifater_res)
                else:
                    break
        elif option == 5:
            break
        else:
            print("Wrong option")


def customer_menu():
    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    customer = Customer(name=name, email=email, address=address)
    while True:
        print(f"--- {customer.name}'s Menu ---")
        print("1. View Restaurant Menu")
        print("2. View Balance")
        print("3. Add Balance")
        print("4. Place Order")
        print("5. View Past Orders")
        print("6. Pay bill")
        print("7. Exit")

        option = int(input("Enter an option: "))

        if option == 1:
            customer.view_menu(rifater_res)
        elif option == 2:
            customer.view_balance()
        elif option == 3:
            amount = int(input("Enter the amount to add in your balance: "))
            customer.add_balance(amount)
        elif option == 4:
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the item quantity: "))
            customer.add_to_cart(rifater_res, item_name, quantity)
        elif option == 5:
            customer.view_cart()
        elif option == 6:
            customer.pay_bill()
        elif option == 7:
            break
        else:
            print("Wrong option")


while True:
    print("------Restaurant Management System-----")
    print("1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")

    choice = int(input("Select an option: "))

    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        break
    else:
        print("Wrong option")
