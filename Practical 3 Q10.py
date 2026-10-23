# Display the available operations
print("MENU")
print("1. Check Even or Odd")
print("2. Find Largest of Three Numbers")
print("3. Grade System")

# Accept the user's choice
choice = int(input("Enter your choice (1-3): "))

# Execute the selected operation
if choice == 1:
    number = int(input("Enter an integer: "))

    # Check whether the remainder after division by 2 is zero
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

elif choice == 2:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    # Compare the numbers to identify the largest
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)

elif choice == 3:
    marks = float(input("Enter marks: "))

    # Assign a grade using the Practical 3 criteria
    if marks < 0 or marks > 100:
        print("Invalid marks.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")

else:
    # Handle a choice outside the menu
    print("Invalid choice.")
