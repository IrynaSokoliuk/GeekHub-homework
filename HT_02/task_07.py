#Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and integers and must be hardcoded.

list_1 = ["Hello,", "it's", True, "this is", 7, "task"]

list_str = [str(i) for i in list_1]
result = ' '.join(list_str)

print(result)
