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