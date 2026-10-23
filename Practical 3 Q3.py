# Accept marks from the user
marks = float(input("Enter marks: "))

# Check that marks are within the valid range
if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 90:
    # Marks of 90 or above receive grade A
    print("Grade: A")
elif marks >= 75:
    # Marks from 75 to below 90 receive grade B
    print("Grade: B")
elif marks >= 50:
    # Marks from 50 to below 75 receive grade C
    print("Grade: C")
else:
    # Marks below 50 result in Fail
    print("Grade: Fail")
