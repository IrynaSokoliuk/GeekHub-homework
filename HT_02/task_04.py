#Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.

num = int(input("Введіть число: "))
str = []

for i in range(num):
    user_input = input(f"Введіть строку {i+1}: ")
    str.append(user_input)

result = ''.join(str)

print(f"Результат усіх введених строк: {result}")
