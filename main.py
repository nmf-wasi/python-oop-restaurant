from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order

def customer_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone number: ")
    address=input("Enter your address: ")
    customer=Customer(name=name, email=email, phn_no=phone, address=address)


    sj=Restaurant("Sejong")

    while(True):
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Paybill")
        print("5. Exit")


        choice=int(input("Enter your choice: "))
        if choice==1:
            customer.viewMenuItems(sj)
        elif choice ==2:
            item_name=input("Enter item name: ")
            item_quantity=int(input("Enter item quantity: "))
            customer.addToCart(sj,item_name,item_quantity)
        elif choice==3:
            customer.viewCart()
        elif choice==4:
            customer.payBill()
        elif choice==5:
            break
        else:
            print("Invalid input!")

            

def admin_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone number: ")
    address=input("Enter your address: ")
    admin=Admin(name=name, email=email, phn_no=phone, address=address)


    sj=Restaurant("Sejong")

    while(True):
        print(f"Welcome {admin.name}")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Remove item")
        print("6. Exit")


        choice=int(input("Enter your choice: "))
        if choice==1:
            item_name=input("Enter new item name: ")
            item_price=int(input("Enter item price: "))
            item_quantity=int(input("Enter item quantity: "))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.addNewItem(sj, item)
        elif choice ==2:
            employee_name=input("Enter employee name: ")
            employee_phone_no=input("Enter employee phone number: ")
            employee_email=input("Enter employee email: ")
            employee_designation=input("Enter employee designation: ")
            employee_age=input("Enter employee age: ")
            employee_address=input("Enter employee address: ")
            employee_salaary=input("Enter employee salary: ")
            employee=Employee(employee_name,employee_email,employee_phone_no,employee_address,employee_age,employee_designation, employee_salaary)
            admin.addEmployee(sj,employee)
        elif choice==3:
            admin.viewEmployee(sj)
        elif choice==4:
            admin.viewMenu(sj)
        elif choice==5:
            item_name=input("Enter item name: ")
            admin.removeItem(sj,item_name)
        elif choice==6:
            break
        else:
            print("Invalid input!")




while(True):
    print("Welcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid Input")
