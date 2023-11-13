"""
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться
    в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
    Кожну 1 секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів -
    логіка така сама як і в звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""


import time


def traffic_light():
    while True:
        for _ in range(4):
            time.sleep(1)
            print("Red - Green")
        for _ in range(2):
            time.sleep(1)
            print("Yellow - Red")
        for _ in range(4):
            time.sleep(1)
            print("Green - Red")
        for _ in range(2):
            time.sleep(1)
            print("Yellow - Red")


traffic_light()
