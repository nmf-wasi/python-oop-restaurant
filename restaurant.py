from menu import Menu
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

