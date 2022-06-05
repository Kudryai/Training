from re import S


while True:
    s = input("Введи что нить:")
    if s == "выход":
        break
    if len(s) < 3:
        print ("маловато")
        continue
    print('введенная строка достаточной длинны') # Разные другие действия здесь