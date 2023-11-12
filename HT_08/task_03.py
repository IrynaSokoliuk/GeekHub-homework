"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
    https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
    Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(start, stop, step=1):
    if stop is None:
        start, stop = 0, start
    current_element = start
    if step > 0:
        while current_element < stop:
            yield current_element
            current_element += step
    elif step < 0:
        while current_element > stop:
            yield current_element
            current_element += step
    else:
        raise ValueError("Step must not be zero")


for i in my_range(1, -10, 5):
    print(i)
