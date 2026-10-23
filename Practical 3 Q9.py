# Accept the lengths of three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check that the sides are positive
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle sides.")
# Check the triangle inequality condition
elif a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot form a triangle.")
elif a == b and b == c:
    # All three sides are equal
    print("Equilateral triangle.")
elif a == b or b == c or a == c:
    # Exactly two sides are equal
    print("Isosceles triangle.")
else:
    # All three sides are different
    print("Scalene triangle.")
