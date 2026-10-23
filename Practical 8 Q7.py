# Practical 8 - Q7: keys(), values(), items()
# Aim: Convert dictionary keys, values, and pairs into lists.

student = {
    "name": "Asha",
    "age": 18,
    "marks": 92
}

keys_list = list(student.keys())
values_list = list(student.values())
items_list = list(student.items())

print("Keys:", keys_list)
print("Values:", values_list)
print("Key-value pairs:", items_list)
