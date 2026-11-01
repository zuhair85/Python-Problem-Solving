# Task: Create a Python inventory management system using a dictionary. Each product should have a name, quantity, and price. Your program should support:
# 1. Adding new products.
# 2. Updating existing product quantities and prices.
# 3. Removing products.
# 4. Displaying the current inventory.
# This problem is a little different from the previous ones. Instead of performing one operation on a dictionary, you'll build several functions that work together.

def add_product(inventory, name, quantity, price):
    # Add a new product to the inventory
    name = name.lower()
    if name.lower() not in inventory:
        inventory[name] = {}
        inventory[name]["quantity"] = quantity
        inventory[name]["price"] = price
    else:
        inventory[name]["quantity"] = inventory[name]["quantity"] + quantity
        inventory[name]["price"] = price

    return inventory

def update_product(inventory, name, quantity=None, price=None):
    # Update the product's quantity and/or price
    if name not in inventory:
        return inventory

    if quantity is not None and price is not None:
        inventory[name]["quantity"] = quantity
        inventory[name]["price"] = price
    elif quantity is not None:
        inventory[name]["quantity"] = quantity
    elif price is not None:
        inventory[name]["price"] = price

    return inventory

def remove_product(inventory, name):
    # Remove a product from inventory
    if name not in inventory:
        return inventory

    #del inventory[name]
    inventory.pop(name)

def display_inventory(inventory):
    # Display all products, quantities, and prices
    if len(inventory) == 0:
        return
    for key in inventory:
        print(f'Product: {key} | Quantity: {inventory[key]["quantity"]} | Price: ${inventory[key]["price"]}')

inventory = {
    "apple": {"quantity": 50, "price": 0.75},
    "banana": {"quantity": 30, "price": 0.50}
}
add_product(inventory, "orange", 40, 0.90)
add_product(inventory, "apple", 10, 0.75)
update_product(inventory, "apple", quantity=80)
update_product(inventory, "apple", price=0.85)
remove_product(inventory, "banana")
remove_product(inventory, "watermelon")
display_inventory(inventory)
# print(inventory)