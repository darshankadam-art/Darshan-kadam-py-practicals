# Accept age and nationality
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").strip()

# First check the age condition
if age >= 18:
    # Check nationality only if the age condition is true
    if nationality.lower() == "indian":
        print("Eligible to vote.")
    else:
        print("Not eligible: nationality must be Indian.")
else:
    print("Not eligible: age must be 18 or above.")
