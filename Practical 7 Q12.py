
# Store shopping cart products in a list
cart = ["Milk", "Bread", "Eggs"]

# Store fixed product categories in a tuple
categories = ("Dairy", "Bakery", "Groceries")

# Add a new product to the cart
cart.append("Rice")

# Remove a product from the cart
cart.remove("Bread")

# Display the updated cart
print("Shopping cart:", cart)

# Display the fixed categories
print("Product categories:", categories)

# Display the cart summary
print("Total items:", len(cart))

# Display each product
print("Cart summary:")
for item in cart:
    print("-", item)
