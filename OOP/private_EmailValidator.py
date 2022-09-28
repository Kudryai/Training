from string import ascii_letters, ascii_uppercase, ascii_lowercase
import random

class EmailValidator:
    STRIP_MAIL = ascii_letters + ascii_lowercase + '1234567890' + '_.'
    CHECK_MAIL = STRIP_MAIL + '@'
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        pattern = 'xxxxxxxxxx'
        res = ''
        for i in range(len(pattern)):
            if pattern[i] == 'x':
                res += random.choice(cls.STRIP_MAIL)
            else:
                res += pattern[i]
        return res + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        cnt = 0
        stop = 0
        if cls.__is_email_str(email):
            if email.count('@') == 1:
                for i in range(len(email)):
                    if email.count('.',0,stop) > 1:
                        return False
                    if email[i] in cls.CHECK_MAIL:
                        cnt += 1
                        if email[i] == '@':
                            stop = i
                            if len(email[:i]) <= 100 and len(email[i+1:]) <= 50:
                                    continue
                        if cnt == len(email):
                            if email.endswith('.ru') or email.endswith('.com'):
                                return True
        return False

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        else:
            return False

        
print(EmailValidator.check_email("sc_lib@list.ru")) #== True
print(EmailValidator.check_email("sc_lib@list_ru")) #== False
print(EmailValidator.check_email("sc@lib@list_ru")) #== False
print(EmailValidator.check_email("sc.lib@list_ru")) #== False
print(EmailValidator.check_email("sclib@list.ru")) #== True
print(EmailValidator.check_email("sc.lib@listru")) #== False
print(EmailValidator.check_email("sc..lib@list.ru")) #== False