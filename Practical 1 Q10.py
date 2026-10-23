# Practical 1 - Q10: Boolean Logic and Data Types
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
age_condition = age > 18
marks_condition = marks > 50
print("Age greater than 18:", age_condition)
print("Marks greater than 50:", marks_condition)
if age_condition and marks_condition:
    print("Both conditions are satisfied.")
elif age_condition:
    print("Only the age condition is satisfied.")
elif marks_condition:
    print("Only the marks condition is satisfied.")
else:
    print("Neither condition is satisfied.")
