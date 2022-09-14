from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    
    def check_card_number(number):
        check = number.split('-')
        if ''.join(check).isdigit() and len(''.join(check).isdigit()) == 16:
            if number[4] == '-' and number[9] == '-' and number[14] == '-':
                return True
        return False

    @classmethod
    def check_name(cls,name):
        ok = 0
        name = name.replace(' ', '')
        for letter in name:
            if letter in cls.CHARS_FOR_NAME:
                ok += 1
                if ok == len(name):
                    return True
        return False
