store_name = "Hafsa Mart"
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)


class Electronics(Product):
    def __init__(self, name, price, warranty):
        Product.__init__(self, name, price)
        self.warranty = warranty

    def show_electronics(self):
        print(self.name, self.price, "Warranty:", self.warranty)

class Clothing(Product):
    def __init__(self, name, price, size):
        Product.__init__(self, name, price)
        self.size = size

    def show_clothing(self):
        print(self.name, self.price, "Size:", self.size)



class Cart:
    def __init__(self):
        self.total = 0

    def add(self, price):
        self.total += price

    def checkout(self):
        print("Store:", store_name) 

        print("Total:", self.total)

        discount = 0.1  
        final = self.total - (self.total * discount)

        print("Final Price:", final)


p1 = Electronics("Laptop", 100000, "1 year")
p2 = Clothing("Shirt", 2000, "M")

p1.show_electronics()
p2.show_clothing()

cart = Cart()
cart.add(p1.price)
cart.add(p2.price)

cart.checkout()

