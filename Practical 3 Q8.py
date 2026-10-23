# Accept the purchase amount
amount = float(input("Enter purchase amount: "))

# Check for a valid non-negative purchase amount
if amount < 0:
    print("Invalid purchase amount.")
elif amount >= 2000:
    # Apply a 20% discount for purchases of Rs. 2000 or above
    discount = amount * 20 / 100
    final_amount = amount - discount
elif amount >= 1000:
    # Apply a 10% discount for purchases of Rs. 1000 or above
    discount = amount * 10 / 100
    final_amount = amount - discount
else:
    # No discount for purchases below Rs. 1000
    discount = 0
    final_amount = amount

# Display the discount and final amount
if amount >= 0:
    print(f"Discount: Rs. {discount:.2f}")
    print(f"Final Amount: Rs. {final_amount:.2f}")
