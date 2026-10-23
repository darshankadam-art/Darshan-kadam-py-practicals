# Accept a year from the user
year = int(input("Enter a year: "))

# Apply the leap year rules
if year % 400 == 0:
    # Years divisible by 400 are leap years
    print("It is a leap year.")
elif year % 100 == 0:
    # Years divisible by 100 but not 400 are not leap years
    print("It is not a leap year.")
elif year % 4 == 0:
    # Other years divisible by 4 are leap years
    print("It is a leap year.")
else:
    # All remaining years are not leap years
    print("It is not a leap year.")
