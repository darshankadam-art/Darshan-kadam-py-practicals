
# Create a tuple with repeated elements
colours = ("Red", "Blue", "Green", "Blue", "Yellow", "Blue")

# Count occurrences of Blue
print("Count of Blue:", colours.count("Blue"))

# Find the first index of Blue
print("First index of Blue:", colours.index("Blue"))

# Handle an element that is absent
try:
    print("Index of Black:", colours.index("Black"))
except ValueError:
    print("Black is not present in the tuple.")
