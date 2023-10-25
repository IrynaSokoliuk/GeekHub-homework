"""
Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
Кожне введене значення спочатку пробує перевести в int. 
У разі помилки - пробує перевести в float, а якщо і там ловить помилку - пропонує ввести значення ще раз 
(зручніше на даному етапі навчання для цього використати цикл while)
Виводить результат ділення першого на друге. 
Якщо при цьому виникає помилка - оброблює її і виводить відповідне повідомлення
"""

#Task 1 (a)
is_ok = False

while not is_ok:
    number_1 = input("Write a number 1: ")
    number_2 = input("Write a number 2: ")

    try:
        try:
            number_1 = int(number_1)
            number_2 = int(number_2)
            is_ok = True
        except ValueError:
            number_1 = float(number_1)
            number_2 = float(number_2)
            is_ok = True
    except ValueError:
        print("Try again :c")

print(f"My numbers: {number_1}, {number_2}")

# Task 1 (b)
try:
    result = number_1 / number_2
except ZeroDivisionError:
    print("Oh no....Try again... ")
else:
    print(f"Result is: {round(result, 2)}")
