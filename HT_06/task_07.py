"""
Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньомy і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""


def uniq_values_counter(my_list):
    uniq_vals = {}
    for el in my_list:
        if isinstance(el, (list, bool)):
            el = str(el)

        if el in uniq_vals:
            uniq_vals[el] += 1
        else:
            uniq_vals[el] = 1

    return uniq_vals


l = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]
print(uniq_values_counter(l))
