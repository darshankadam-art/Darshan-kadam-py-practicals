# Practical 1 - Q7: Memory Behavior of Variables
a = 100
b = 100
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))
print("Same object initially:", a is b)
a = 200
print("After changing a:")
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))
# Integers are immutable; reassignment changes what a refers to.
