# Practical 1 - Q4: Data Type Identification System
integer_value = int(input("Enter an integer: "))
float_value = float(input("Enter a float: "))
string_value = input("Enter a string: ")

boolean_input = input("Enter True or False: ").strip().lower()
if boolean_input == "true":
    boolean_value = True
elif boolean_input == "false":
    boolean_value = False
else:
    raise ValueError("Enter either True or False.")

values = [
    ("Integer", integer_value),
    ("Float", float_value),
    ("String", string_value),
    ("Boolean", boolean_value)
]
print("\nType summary:")
print(f"{'Value':<20} {'Type':<15}")
print("-" * 35)
for label, value in values:
    print(f"{str(value):<20} {type(value).__name__:<15}")
