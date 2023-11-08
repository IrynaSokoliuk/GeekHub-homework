"""
Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж)
і повертає генератор, який буде вертати значення з цієї послідовності,
при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in generator([1, 2, 3]):
       print(elem)
   1
   2
   3
   1
   2
   3
   1
   .......
"""


def infinity_generation(itr_obj):
    start_obj = itr_obj
    index = 0
    max_index = len(itr_obj)
    while True:
        for i in itr_obj:
            index += 1
            if index == max_index:
                itr_obj = start_obj
            yield i


g = infinity_generation("122")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
