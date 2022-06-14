print('Добро пожаловать в Шифратор/Дешифратор')
txt = input('Введи текст для шифрования/дешифрования: ')
def check(txt):
    if txt == 'de':
        return txt
    if txt == 'sh':
        return txt
    if txt == 'rus':
        return txt
    if txt == 'eng':
        return txt
    if txt.isdigit() == True:
        if int(txt) < 32:
            return txt
    else:
        return False


def shifr(met,lang,sec):
    ready_txt = ''
    if met == 'de':
        if lang == 'eng':
            for i in range(len(txt)):
                if 65 <= ord(txt[i]) <= 90:
                    b = ord(txt[i]) - int(sec)
                    if b < 65:
                        b += 26
                    if b > 90:
                        b -= 26
                    ready_txt += chr(b)
                    continue
                if 97 <= ord(txt[i]) <= 122:
                    b = ord(txt[i]) - int(sec)
                    if b < 97:
                        b += 26
                    if b > 122:
                        b -= 26
                    ready_txt += chr(b)
                    continue
                if ord(txt[0]) > 1040:
                    print('Выбран не тот язык')
                    break
                else:
                    ready_txt += txt[i]
        if lang == 'rus':
            for i in range(len(txt)):
                if 1040 <= ord(txt[i]) <= 1071:
                    b = ord(txt[i]) - int(sec)
                    if b < 1040:
                        b += 32
                    if b > 1071:
                        b -= 32
                    ready_txt += chr(b)
                    continue
                if 1072 <= ord(txt[i]) <= 1103:
                    b = ord(txt[i]) - int(sec)
                    if b < 1072:
                        b += 32
                    if b > 1103:
                        b -= 32
                    ready_txt += chr(b)
                    continue
                if ord(txt[0]) < 700:
                    print('Выбран не тот язык')
                    break
                else:
                    ready_txt += txt[i]
    if met == 'sh':
        if lang == 'eng':
            for i in range(len(txt)):
                if 65 <= ord(txt[i]) <= 90:
                    b = ord(txt[i]) + int(sec)
                    if b < 65:
                        b += 26
                    if b > 90:
                        b -= 26
                    ready_txt += chr(b)
                    continue
                if 97 <= ord(txt[i]) <= 122:
                    b = ord(txt[i]) + int(sec)
                    if b < 97:
                        b += 26
                    if b > 122:
                        b -= 26
                    ready_txt += chr(b)
                    continue
                if ord(txt[0]) > 1000:
                    print('Выбран не тот язык')
                    break
                else:
                    ready_txt += txt[i]
        if lang == 'rus':
            for i in range(len(txt)):
                if ord(txt[0]) < 700:
                    print('Выбран не тот язык')
                    break
                if 1040 <= ord(txt[i]) <= 1071:
                    b = ord(txt[i]) + int(sec)
                    if b < 1040:
                        b += 32
                    if b > 1071:
                        b -= 32
                    ready_txt += chr(b)
                    continue
                if 1072 <= ord(txt[i]) <= 1103:
                    b = ord(txt[i]) + int(sec)
                    if b < 1072:
                        b += 32
                    if b > 1103:
                        b -= 32
                    ready_txt += chr(b)
                    continue
                else:
                    ready_txt += txt[i]
    return print(ready_txt)

while True:
    road = input('Какой направление необходимо? DE - дешифрование, SH - шифрование: ').lower()
    if check(road) != road:
        print('Неверный ввод')
    if check(road) == road:
        break

while True:
    langua = input('Какой язык текста необходим? RUS - русский, ENG - английский: ').lower()
    if check(langua) != langua:
        print('Неверный ввод')
    if check(langua) == langua:
        break

while True:
    kod = input('Какой шаг силы сдвига для шифрования/дешифрования: ')
    if check(kod) != kod:
        print('Неверный ввод')
    if check(kod) == kod:
        shifr(road,langua,kod) 
        break

