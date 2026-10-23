# Practical 8 - Q9: Nested Dictionary
# Aim: Create nested student details, access values, and modify data.

students = {
    "S101": {"name": "Asha", "age": 18, "marks": 85},
    "S102": {"name": "Ravi", "age": 19, "marks": 90}
}

print("S101 student name:", students["S101"]["name"])
print("S102 marks:", students["S102"]["marks"])

students["S101"]["marks"] = 95

print("Updated S101 marks:", students["S101"]["marks"])
print("Updated student details:", students)
