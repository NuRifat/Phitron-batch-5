from menu import Menu


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
