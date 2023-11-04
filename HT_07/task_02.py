"""
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""


class InvalidDataException(Exception):
    pass


def validation(name, password):
    name = str(name)
    password = str(password)
    if (
            3 < len(name) < 50
            and len(password) > 8
            and any(ch.isdigit() for ch in password)
            and len(password) < 27
    ):
        return True
    else:
        raise InvalidDataException


validation("Iryna", "somepassword123")
