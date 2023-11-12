"""
Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
 Файл також додайте в репозиторій. На екран повинен вивестись список
 із трьома блоками - символи з початку, із середини та з кінця файлу.
  Кількість символів в блоках - та, яка введена в другому параметрі.
  Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або,
   наприклад, файл із двох символів і треба вивести по одному символу,
   то що виводити на місці середнього блоку символів?).
Не забудьте додати перевірку чи файл існує.
"""


def process_file(file_path, qty_symbols):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if qty_symbols > len(content):
                raise ValueError("Кількість символів більша, ніж загальна кількість символів у файлі.")

            middle_index = len(content) // 2
            middle_block = content[middle_index - qty_symbols // 2: middle_index + qty_symbols // 2]

            print(f"Початок файлу: {content[:qty_symbols]}")
            print(f"Середина файлу: {middle_block}")
            print(f"Кінець файлу: {content[-qty_symbols:]}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except ValueError as ex:
        print(f"Помилка: {ex}")


file_path = "task_2.txt"
qty_symbols = 4

process_file(file_path, qty_symbols)
