# Practical 1 - Q5: Type Conversion (Casting)
try:
    age_text = input("Enter your age: ")
    marks_text = input("Enter your marks: ")
    age = int(age_text)
    marks = float(marks_text)
    print("Age next year:", age + 1)
    print("Marks after adding 5:", marks + 5)
    # Without conversion, strings concatenate instead of adding numerically.
    print("Without conversion, age + '1' gives:", age_text + "1")
except ValueError:
    print("Invalid input: enter a whole-number age and numeric marks.")
