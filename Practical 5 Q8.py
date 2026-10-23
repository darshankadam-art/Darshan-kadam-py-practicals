# Define the correct password for this exercise
correct_password = "python123"

# Allow a maximum of three attempts
for attempt in range(1, 4):
    password = input("Enter password: ")

    # Check whether the entered password is correct
    if password == correct_password:
        print("Login successful.")

        # Stop after a correct password
        break

    print("Incorrect password.")

# The loop's else block runs if no break occurred
else:
    print("Login failed. All 3 attempts used.")
