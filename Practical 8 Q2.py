# Practical 8 - Q2: Accessing Values
# Aim: Access dictionary values by key and handle a missing key.

student = {"Name": "Asha", "Age": 18, "Marks": 92}

print("Name:", student["Name"])
print("Age:", student["Age"])
print("Marks:", student["Marks"])

try:
    print(student["Grade"])
except KeyError:
    print("Error: The key 'Grade' does not exist.")
