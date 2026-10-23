# Practical 8 - Q11: Sorting Dictionary Data
# Aim: Sort a dictionary by keys and by values.

marks = {
    "Ravi": 85,
    "Asha": 92,
    "Neha": 78,
    "Ujjwal": 88
}

sorted_by_keys = dict(sorted(marks.items()))
sorted_by_values = dict(sorted(marks.items(), key=lambda item: item[1]))

print("Sorted by keys:")
print(sorted_by_keys)

print("Sorted by values:")
print(sorted_by_values)
