from restaurant import Restaurant
from user import Admin
from user import Customer
from food_item import Food_item

rifater_res = Restaurant("Welcome to Rifat's Restaurant")


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
                print("1. Add Item")
                print("2. Remove Item")
                print("3. View Items")
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
        print(f"---Welcome {customer.name} to our Restaurant---")
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
