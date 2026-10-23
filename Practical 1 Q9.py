# Practical 1 - Q9: Data Type-Based Calculator
# Parse inputs as integers/floats where possible; otherwise treat them as strings.
def parse_value(text):
    text = text.strip()
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text

first = parse_value(input("Enter the first value: "))
second = parse_value(input("Enter the second value: "))

if isinstance(first, (int, float)) and isinstance(second, (int, float)):
    print("Detected type: numeric")
    print("Addition:", first + second)
elif isinstance(first, str) and isinstance(second, str):
    print("Detected type: string")
    print("Concatenation:", first + second)
else:
    print("Invalid combination: enter two numeric values or two strings.")
