#Write a script to check whether a value from user input is contained in a group of values.
#    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#         [1, 2, 'u', 'a', 4, True] --> 5 --> False

my_list = [1, 2, 'u', 'a', 4, True]
list_str = [str(i) for i in my_list]
user_value = input("Введіть значення для перевірки: ")

if user_value in list_str:
	print(True)
else:
    print(False)
