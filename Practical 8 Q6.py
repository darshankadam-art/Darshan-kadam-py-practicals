# Practical 8 - Q6: Iterating Through a Dictionary
# Aim: Print keys, values, and key-value pairs using loops.

student = {
    "name": "Asha",
    "age": 18,
    "marks": 92
}

print("Dictionary keys:")
for key in student:
    print(key)

print("Dictionary values:")
for value in student.values():
    print(value)

print("Key-value pairs:")
for key, value in student.items():
    print(key, ":", value)
