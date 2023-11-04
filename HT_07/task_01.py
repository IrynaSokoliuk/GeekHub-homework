"""
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
 Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
  і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException (його також треба створити =))
"""


class LoginException(Exception):
    pass


def security(username, password, silent=False):
    db = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }

    if username in db and str(password) == str(db[username]):
        return True
    else:
        if silent is True:
            return False
        else:
            raise LoginException("Error")


result = security()
print(f"Result login is {result}")
