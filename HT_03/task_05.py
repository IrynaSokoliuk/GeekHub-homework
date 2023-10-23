'''
Write a script to remove values duplicates from dictionary.
Feel free to hardcode your dictionary.
'''

dict_1 = {'fruit': 'apple', 'fruit_1': 'apple', 'fruit_2': 'banana'}
dict_2 = {}

for key, value in dict_1.items():
    if value not in dict_2.values():
        dict_2[key] = value

print(dict_2)
