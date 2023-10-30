'''
Наприклад маємо рядок --> 
"f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> 
просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
'''

string_1 = ("f98neroi4nr0c3n30irn03ien3c0rfe  "
            "kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 "
            "65jnpoj35po6j345")


def random_string(my_str):
    digit_count = ""
    alpha_count = ""

    for el in my_str:
        if el.isdigit():
            digit_count += el
        elif el.isalpha():
            alpha_count += el

    if 30 <= len(my_str) <= 50:
        print(f"Довжина рядка: {len(my_str)}\n"
              f"Кількість букв: {len(alpha_count)}\n"
              f"Кількість цифр: {len(digit_count)}")

    elif 30 > len(my_str):
        sum_digit_count = 0
        for elem in digit_count:
            sum_digit_count += int(elem)
        print(f"Сума усіх цифр: {sum_digit_count}\n"
              f"Рядок без цифр: {alpha_count} ")

    elif 50 < len(my_str):
        uniq_elements = set(my_str)
        res = "".join(uniq_elements)
        print(f"Оновлений рядок: {res}")


random_string(string_1)
