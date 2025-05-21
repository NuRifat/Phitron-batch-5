from food_item import FoodItem
from user import Customer, Admin, Employee
from restaurant import Restaurant

megpai_res = Restaurant("Megpai Restaurant")


def customer_menu():
    name = input('Enter your name : ')
    email = input('Enter your Email : ')
    phone = input('Enter your Phone : ')
    address = input('Enter your Address : ')
    customer = Customer(name=name, phone=phone, email=email, address=address)

    while True:
        print(f'Welcome {customer.name}!!')
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. view Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input('Enter your choice: '))
        if choice == 1:
            customer.view_menu(megpai_res)
        elif choice == 2:
            item_name = input("Enter Item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(megpai_res, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid")


def admin_menu():
    name = input('Enter your name : ')
    email = input('Enter your Email : ')
    phone = input('Enter your Phone : ')
    address = input('Enter your Address : ')
    admin = Admin(name=name, phone=phone, email=email, address=address)

    while True:
        print(f'Welcome {admin.name}!!')
        print("1. Add new item")
        print("2. Add new employee")
        print("3. view employee")
        print("4. view items")
        print("5. delete item")
        print("6. Exit")

        choice = int(input('Enter your choice: '))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(megpai_res, item)

        elif choice == 2:
            name = input("Enter Employee Name : ")
            phone = int(input("Enter Employee phone : "))
            email = input("Enter Employee Email : ")
            designation = input("Enter Employee designation : ")
            age = int(input("Enter Employee age : "))
            salary = int(input("Enter Employee salary : "))
            address = input("Enter Employee address : ")
            employee = Employee(name, phone, email, address,
                               age, designation, salary)
            admin.add_employee(megpai_res,employee)
        elif choice == 3:
            admin.view_employee(megpai_res)
        elif choice == 4:
            admin.view_menu(megpai_res)
        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.remove_item(megpai_res, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid")


while True:
    print("Welcome!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input('Enter your choice: '))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid")
