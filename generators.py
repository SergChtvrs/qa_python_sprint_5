import random
import secrets
import string


class AuthGenerator:
    user_name = "Sergey"

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def login_generator(self):
        name = "sergey"
        last_name = "chetverous"
        cohort = "fs06"
        domain = "@yandex.ru"
        self.login = name + last_name + cohort + str(random.randint(100, 999)) + domain
        return self.login

    def correct_password_generator(self):
        alphabet = string.ascii_letters + string.digits
        self.password = ''.join(secrets.choice(alphabet) for i in range(6))
        return self.password
