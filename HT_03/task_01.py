'''
Write a script that will run through a list of tuples
and replace the last value for each tuple. The list of
tuples can be hardcoded. The "replacement" value is entered by user.
The number of elements in the tuples must be different.
'''

value = input("Enter a value: ")

list_of_tuples = [(), (99,), (1, 2, 3)]

new_list = []

for tuple_ in list_of_tuples:
    tmp_list = list(tuple_)
    if len(tuple_) > 0:
        tmp_list[-1] = value
        new_list.append(tuple(tmp_list))
    else:
        tmp_list.append(value)

print(new_list)
