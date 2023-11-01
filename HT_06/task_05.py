"""
Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі,
що не перевищують його.

"""


def fibonacci(element):
    a, b = 0, 1
    while a <= element:
        print(a, end=" ")
        a, b = b, a + b


fibonacci()
