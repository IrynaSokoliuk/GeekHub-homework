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
    db = [
        {"username": "Alina", "password": "1g^fhjmgasc"},
        {"username": "Alika", "password": "2JK7dfg&D62gfefk"},
        {"username": "Apika", "password": "3SDKU^rFDSU"},
        {"username": "Aladin", "password": "4sdf"},
        {"username": "Alan", "password": "5sdf"}
    ]

    for i in db:
        if i["username"] == username and i["password"] == password:
            print(username)
            return True

    if silent is True:
        return False
    else:
        raise LoginException("Error")


result = security("Alan", "5sdf")
print(f"Result login is {result}")
