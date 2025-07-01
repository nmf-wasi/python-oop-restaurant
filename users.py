from abc import ABC
from menu import Menu
from orders import Order

class User(ABC):
    def __init__(self, name, email, phn_no, address):
        self.name = name
        self.email = email
        self.phn_no = phn_no
        self.address = address




class Customer(User):
    def __init__(self, name, email, phn_no, address):
        super().__init__(name, email, phn_no, address)
        self.cart = Order()

    def viewMenuItems(self, restaurant):
        restaurant.menu.showMenuItems()

    def addToCart(self, restaurant, item_name, quantity):
        item = restaurant.menu.findItem(item_name)  # search if the item customer is looking for exists
        if item:
            if quantity>item.quantity:
                print("Item Quantity exceeded!")
            else:
                item.quantity = quantity
                self.cart.addItem(item)
                print("Item Added!")
        else:
            print("Item not found!")

    def payBill(self):
        print(f"Total {self.cart.totalPrice} paid successfully!")
        self.cart.clear()

    def viewCart(self):
        print("*****CART*****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")  # -> item name and price from us, quantity from user
        print(f"Total price:{self.cart.totalPrice}")

class Employee(User):
    def __init__(self, name, email, phn_no, address, age, designation, salary):
        super().__init__(name, email, phn_no, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phn_no, address):
        super().__init__(name, email, phn_no, address)

    def addEmployee(self, restaurant, employee):  # restaurant is an object
        restaurant.addEmployee(employee)  # we are calling addEmployee fucntion of restaurant object to add new employees

    def viewEmployee(self, restaurant):
        restaurant.viewEmployee()

    def addNewItem(self, restaurant, item):
        restaurant.menu.addMenuItem(item)

    def removeItem(self, restaurant, item):
        restaurant.menu.removeItem(item)

    def viewMenu(self, restaurant):
        restaurant.menu.showMenuItems()