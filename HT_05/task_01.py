'''
Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) 
та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь). 
У випадку некоректного введеного значення - виводити відповідне повідомлення.
'''


def season(month: int):
    if month in [1, 2, 12]:
        print("Вашій цифрі відповидає пора року - Зима")
    elif month in [3, 4, 5]:
        print("Вашій цифрі відповидає пора року - Весна")
    elif month in [6, 7, 8]:
        print("Вашій цифрі відповидає пора року - Літо")
    elif month in [9, 10, 11]:
        print("Вашій цифрі відповидає пора року - Осінь")
    else:
        print("Ви ввели некоректні дані!")


month = int(input("Введіть номер місяця (від 1 до 12): "))
season(month)
