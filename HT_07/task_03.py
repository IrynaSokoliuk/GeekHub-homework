"""
На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити словник із парами ім'я/пароль різноманітних видів
   (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому словнику і,
    користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень
    відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""

db = {
    "G": "password1",
    "GeekHub": "passsssword",
    "GeekHub1": "pasword1",
    "GeekHub2": "password2",
    "GeekHub3": "pass3",
    "GeekHub4": "password1!"
}


class InvalidDataException(Exception):
    pass


def has_special_symbol(password):
    special = ["!", "*", "#", "@", "?"]
    for i in password:
        if i in special:
            return True
    return False


def validator(log, passw):
    log = str(log)
    passw = str(passw)
    if not 3 < len(log) < 50:
        raise InvalidDataException("name is less than 3 or more than 50")
    elif not len(passw) > 8:
        raise InvalidDataException("password is less than 8")
    elif not any(ch.isdigit() for ch in passw):
        raise InvalidDataException("password must have at least one digit")
    elif not has_special_symbol(password):
        raise InvalidDataException("password should have at least 1 special symbol")
    else:
        return "OK"


if __name__ == "__main__":
    for name, password in db.items():
        try:
            status = validator(name, password)
        except InvalidDataException as ex:
            status = ex
        print("-"*10)
        print(f"Name: {name}\nPassword: {password}\nStatus: {status}")
