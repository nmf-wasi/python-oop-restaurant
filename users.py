from abc import ABC


class User(ABC):
    def __init__(self, name, email, phn_no, address):
        self.name = name
        self.email = email
        self.phn_no = phn_no
        self.address = address


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
        self.menu = Menu() #-> this will create an object named Menu in the restuarant class, then it will use Menu() to acess that class. 
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
item = FoodItem("Pizza", 12.45, 10)
mn.addMenuItem(item)
mn.showMenuItems()
