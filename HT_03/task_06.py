"""
Write a script to get the maximum and minimum value in a dictionary.
"""

dict_1 = {'a': 5, 'b': 6, 'c': 7, 'd': 10, 'e': [1, 2, 3], 'f': "value", 'g': 123.124}

dict_value = []

for value in dict_1.values():
    if type(value) in (int, float):
        dict_value.append(value)

max_value = max(dict_value)
min_value = min(dict_value)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
