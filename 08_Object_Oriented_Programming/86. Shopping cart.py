# Task: Implement a shopping cart that stores products, quantities, prices, and a running total.

# THIS PROGRAM IS UNFINISHED

class ShoppingCart:

    def __init__(self):
        self.products = {}
        self.total = 0.0

    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name]["quantity"] += quantity
        else:
            self.products[name] = {}
            self.products[name]["price"] = price
            self.products[name]["quantity"] = quantity
        self.total += (price * quantity)


    def remove_product(self, name):
        if name not in self.products:
            print('Product is not in the cart!')
            return
        else:
            self.total -= (self.products[name]["price"] * self.products[name]["quantity"])
            del self.products[name]

    def update_quantity(self, name, quantity):
        if name not in self.products:
            print('Product is not in the cart!')
            return
        else:
            self.products[name]["quantity"] = quantity

    def calculate_total(self):
        return self.total

    def display_cart(self):
        print('Shopping Cart:')
        for product in self.products:
            print(f'{product}   | Price: ${self.products[product]["price"]:.2f} | Quantity: {self.products[product]["quantity"]} | Subtotal: ${self.products[product]["quantity"] * self.products[product]["price"]}')
        print(f'Total: ${self.total}')
cart = ShoppingCart()

cart.add_product("Laptop", 899.99, 1)
cart.add_product("Mouse", 25.50, 2)
cart.add_product("Keyboard", 75.00, 1)
# cart.remove_product("Mouse")

cart.display_cart()
# print(cart.products)
# print(cart.calculate_total())