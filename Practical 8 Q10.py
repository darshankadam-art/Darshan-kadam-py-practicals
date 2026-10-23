# Practical 8 - Q10: Dictionary Merging
# Aim: Merge two dictionaries using update() and observe overwritten keys.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"c": 300, "d": 40}

dict1.update(dict2)

print("Merged dictionary:", dict1)
