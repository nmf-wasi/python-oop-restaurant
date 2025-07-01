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

    @property #->when we call this func, we dont need to use it with (), we can simply use the name of the func
    def totalPrice(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}
