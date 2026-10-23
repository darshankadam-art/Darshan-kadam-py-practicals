# Practical 8 - Q8: Counting Character Frequency
# Aim: Count each character in an input string using a dictionary.

text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for char, count in frequency.items():
    print(repr(char), ":", count)
