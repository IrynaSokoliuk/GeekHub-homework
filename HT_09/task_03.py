"""
Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>)
      та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
      (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал
      додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
      Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
       (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
"""

import csv
import json


def is_number_positive(num: int):
    if num > 0:
        return True


def write_to_balance_txt(username, value):
    with open(f"{username}_balance.txt", "w") as f:
        f.write(str(value))


def get_balance_from_balance_txt(username) -> int:
    with open(f"{username}_balance.txt") as f:
        return int(f.read())


def write_balance_json(username, amount):
    with open(f"{username}_transactions.json", "w") as f:
        f.write(json.dumps(amount))


def add_transaction(username, type_transaction, amount):
    with open(f"{username}_transactions.json") as f:
        data = json.load(f)
        data.append({"transaction_type": type_transaction, "amount": amount})
    with open(f"{username}_transactions.json", "w") as f:
        write_balance_json(username, data)


def create_or_refresh_files():
    data = [
        ["tom", 123456],
        ["bob", 34567],
        ["anna", 89073],
        ["1", 1],
        ["sara", 458933],
    ]
    # create users.csv
    with open("users.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

    default_amount_of_money = 1000
    for user in data:
        username = user[0]

        # create balance files
        write_to_balance_txt(username, default_amount_of_money)

        # create transaction files
        write_balance_json(username, [])


def login():
    username = input("Введіть ім'я: ")
    password = input("Введіть пароль: ")
    with open("users.csv") as f:
        reader = csv.reader(f)
        for user in reader:
            if user[0] == username and user[1] == password:
                print("Вхід успішний!")
                return username
        else:
            print("Неправильні данні. До побачення!")


def view_balance(username):
    balance = get_balance_from_balance_txt(username)
    print(f"Ваш баланс: {balance}\n\n")
    main_menu(username)


def put_cash(username):
    try:
        amount = int(input("Введіть суму на яку хочете поповнити баланс: "))
        if not is_number_positive(amount):
            raise ValueError
        balance = get_balance_from_balance_txt(username)
        result = balance + amount
        write_to_balance_txt(username, result)
        print(f"Ваш баланас тепер становить - {result}\n\n")
        add_transaction(username, "put_cash", amount)
    except ValueError:
        print("Дані не валідні!\n\n")
    main_menu(username)


def get_cash(username):
    try:
        amount = int(input("Введіть суму яку хочете зняти з балансу: "))
        if not is_number_positive(amount):
            raise ValueError

        balance = get_balance_from_balance_txt(username)

        if balance >= amount:
            result = balance - amount
            write_to_balance_txt(username, result)
            print(f"Ваш баланас тепер становить - {result}\n\n")
            add_transaction(username, "get_cash", amount)
        else:
            print("Бажана сума більша за ваш баланс.\n\n")
    except ValueError:
        print("Дані не валідні!\n\n")
    main_menu(username)


def start():
    username = login()
    if not username:
        return

    main_menu(username)


def main_menu(username):
    print("Оберіть необхідну дію:\n1. Продивитись баланс\n2. Зняти кеш\n3. Поповнити баланс\n4. Вихід")
    action = input("\nНапишіть відповідний номер: ")
    print()
    if action == "1":
        view_balance(username)
    elif action == "2":
        get_cash(username)
    elif action == "3":
        put_cash(username)
    elif action == "4":
        print("Вихід")
        return


if __name__ == "__main__":
    create_or_refresh_files()
    start()
