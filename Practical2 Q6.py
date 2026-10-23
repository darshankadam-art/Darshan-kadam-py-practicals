
import math

try:
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    radius = float(input("Enter circle radius: "))

    rectangle_area = length * width
    rectangle_perimeter = 2 * (length + width)

    circle_area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print("\nRectangle")
    print(f"Area: {rectangle_area:.2f}")
    print(f"Perimeter: {rectangle_perimeter:.2f}")

    print("\nCircle")
    print(f"Area: {circle_area:.2f}")
    print(f"Circumference: {circumference:.2f}")

except ValueError:
    print("Invalid input! Please enter a number for every measurement.")
