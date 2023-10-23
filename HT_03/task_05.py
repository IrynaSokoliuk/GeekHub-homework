#Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

dict_01 = {'каша':'гречка', 'каша':'рис', 'фрукт':'яблоко'}
unique_dict = []

for i in dict_01:
    if i in unique_dict:
        continue
        print(unique_dict)