# Practical 8 - Q12: Inventory System
# Aim: Add a product, update stock, remove a product, and show final inventory.

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

inventory["Monitor"] = 8
inventory["Laptop"] = 12
removed_quantity = inventory.pop("Mouse")

print("Removed Mouse quantity:", removed_quantity)
print("Final inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)

total_stock = sum(inventory.values())
print("Total stock units:", total_stock)
