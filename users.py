from abc import ABC


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
            item.quantity = quantity
            self.cart.addItem(item)
            print("Item Added!")
        else:
            print("Item not found!")

    def viewCart(self):
        print("*****CART*****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")  # -> item name and price from us, quantity from user
        print(f"total price:{self.cart.total_price}")


class Order:
    def __init__(self):
        self.items = {}  # cart

    def addItem(self, item):
        if item in self.items:
            self.items[item] += item.quantity  # if the item is already in cart, then increase count
        else:
            self.items[item] = item.quantity  # if not in cart, dont increase count

    def removeItem(self, item):
        if item in self.items:
            del self.items[item]

    def totalPrice(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}


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


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []  # database for employee
        self.menu = (Menu())  # -> this will create an object named Menu in the restuarant class, then it will use Menu() to acess that class.
        # When admin calss is using restaurant class, it can use restaurant.menu.methodName() to use the methods in menu class as well

    def addEmployee(self, employee):
        self.employees.append(employee)

    def viewEmployee(self):
        print("Employee List!!")
        for x in self.employees:
            print(f"{x.name}, {x.email}, {x.phn_no}, {x.address}")


class Menu:
    def __init__(self):
        self.items = []  # database for items

    def addMenuItem(self, item):
        self.items.append(item)

    def findItem(self, itemName):
        for x in self.items:
            if x.name.lower() == itemName.lower():
                return x
        return None

    def removeItem(self, itemName):
        item = self.findItem(itemName)
        if item:
            self.items.remove(item)
            print("Item deleted!")
        else:
            print("Item not found!")

    def showMenuItems(self):
        print("***********Showing Menu Item***********")
        print(f"Name\tPrice\tQuantity")
        for i in self.items:
            print(f"{i.name}\t {i.price}\t {i.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


mn = Menu()
item1 = FoodItem("Pizza", 12.45, 10)
mn.addMenuItem(item1)
item2 = FoodItem("Burger", 15, 10)
mn.addMenuItem(item2)
item3 = FoodItem("KAcchi", 124.5, 10)
mn.addMenuItem(item3) 
# mn.showMenuItems() -> if we add menu items like this, when the Menu class is called, the Menu becomes an empty list, 
# therefore, we need to have an admin to add items
res1=Restaurant("Sejong")
ad=Admin("Wasi","wasi7741@gmail.com",1644341633, "seoul")
ad.addNewItem(res1,item1)
ad.addNewItem(res1,item2)
ad.addNewItem(res1,item3)
c1=Customer("Kel", "Kel@gmail.com", 125423, "Jakarta")
c1.viewMenuItems(res1)



