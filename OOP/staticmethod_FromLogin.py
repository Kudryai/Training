from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
        else:
            raise ValueError("некорректное поле name")
        
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        g = 0
        if 3 <= len(name) <= 50:
            for i in range(len(name)):
                if name[i] in cls.CHARS_CORRECT:
                    g += 1
                    if len(name) == g:
                        return True
        return False

class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        g = 0
        if 3 <= len(name) <= 50:
            for i in range(len(name)):
                if name[i] in cls.CHARS_CORRECT:
                    g += 1
                    if len(name) == g:
                        return True
        return False

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])



# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(html)