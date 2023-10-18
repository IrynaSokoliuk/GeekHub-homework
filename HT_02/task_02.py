#Write a script which accepts two sequences of comma-separated colors from user.
#Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

list_1 = input("Write a random colors of comma-separated: ")
list_2 = input("Write a colors do you like of comma-separated: ")

color_list_1 = list_1.split(', ')
color_list_2 = list_2.split(', ')

result = list(set(color_list_1) - set(color_list_2))
print(result)
