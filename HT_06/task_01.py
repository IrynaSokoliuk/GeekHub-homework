"""
Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення у вигляді кортежа: периметр квадрата,
площа квадрата та його діагональ.
"""


import math

side_square = int(input("Напищіть чому дорівнює сторона квадрата: "))


def square(side_square):
    perimeter = side_square * 4
    area = side_square ** 2
    diagonal = math.sqrt(2) * side_square
    print(f"Периметр квадрата: {side_square*4}\nПлоша квадрата: {area}\nДіагональ квадра: {diagonal}")
    return perimeter, area, diagonal


square(side_square)
