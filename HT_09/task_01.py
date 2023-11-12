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


from time import sleep


def traffic_light():
    config = {
        "Red - Green": 4,
        "Yellow - Red": 2,
        "Green - Red": 4,
    }

    while True:
        for lights, qty in config.items():
            for i in range(qty):
                sleep(1)
                print(lights)


traffic_light()
