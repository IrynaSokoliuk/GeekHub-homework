'''
Write a script which accepts a <number> from user and generates
dictionary in range <number> where key is <number> and #value is <number>*<number>
	e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}
'''

number_1 = int(input("Write a number: "))
dict_1 = {}

for number in range(number_1+1):
    dict_1[number] = number * number

print(dict_1)
