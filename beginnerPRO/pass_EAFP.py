class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if string.isdigit():
        raise LetterError
    cz = 0
    for le in string:
        if le.islower():
            cz += 1
            cnt = 0
            for le2 in string:
                if le2.isupper():
                    cnt += 1
            if cnt == 0:
                raise LetterError
    if cz == 0:
        raise LetterError
    for le3 in string:
        if le3.isdigit():
            return True
    raise DigitError
