# Accept an integer from the user
number = int(input("Enter an integer: "))

# Check the remainder after division by 2
if number % 2 == 0:
    # A remainder of zero means the number is even
    print("The number is even.")
else:
    # Any non-zero remainder means the integer is odd
    print("The number is odd.")
