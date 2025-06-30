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
        restaurant.addEmployee(
            employee
        )  # we are calling addEmployee fucntion of restaurant object to add new employees

    def viewEmployee(self, restaurant):
        restaurant.viewEmployee()


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []  # database for employee

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


ad = Admin("Admin", "admin@gmail.com", 12316456, "Seoul")
ad.addEmployee("Lia", "yejisu@gmail.com", 165463, "Gangnam", 20, "Waiter", 12000)
ad.addEmployee("Yeji", "hwyeji@gmail.com", 15463, "Gwangjin-Gu", 22, "Chef", 15000)
ad.viewEmployee()
