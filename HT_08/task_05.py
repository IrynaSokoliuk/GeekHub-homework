"""
Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр,
які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих).
Реалізуйте обчислення за допомогою генератора.
Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі
"""


def count_generator(input_string):
    input_string = input_string.lower()
    repeated_chars_gen = (i for i in set(input_string) if input_string.count(i) > 1)
    return sum(1 for _ in repeated_chars_gen)


test_string = "Hello128449032"
result = count_generator(test_string)
print(result)
