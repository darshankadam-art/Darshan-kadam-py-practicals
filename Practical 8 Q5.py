# Practical 8 - Q5: Removing Elements
# Aim: Remove dictionary entries using pop() and del.

student = {
    "name": "Asha",
    "age": 18,
    "marks": 92,
    "grade": "A"
}

removed_value = student.pop("age")
print("Removed age:", removed_value)
print("After pop():", student)

del student["grade"]
print("After del:", student)

try:
    student.pop("address")
except KeyError:
    print("Error: The key 'address' does not exist.")

try:
    del student["address"]
except KeyError:
    print("Error: Cannot delete missing key 'address'.")
