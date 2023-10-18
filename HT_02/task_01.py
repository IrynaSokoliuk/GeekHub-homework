#Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = input("Write smth 1, 2, 3, 4\n")
numbers_list = numbers.split(", ")

numbers_list = [int(num) for num in numbers_list]

print("list: ", numbers_list)
print("tuple: ", tuple(numbers_list))
