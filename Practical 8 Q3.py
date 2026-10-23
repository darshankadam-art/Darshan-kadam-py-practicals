# Practical 8 - Q3: Using get()
# Aim: Access existing keys and provide defaults for missing keys.

student = {"name": "Asha", "marks": 92}

print("Name:", student.get("name"))
print("Marks:", student.get("marks"))
print("Grade:", student.get("grade", "Not assigned"))
print("Missing key using get():", student.get("grade", 0))

try:
    print(student["grade"])
except KeyError:
    print("Direct indexing error: key 'grade' not found.")
