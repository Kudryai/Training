from random import *
digits = '012345789'
lowercase_letters = 'abcdefghijklmnoprstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
longlst = [] #Длинна паролей
go_psw = [] #Готовые пароли
print('Привет, генератор паролей готов к работе!')
stop = 1
num = 1

def check(choice,che):
    if choice == 'y':
        return True
    if choice == 'n':
        return False
    if choice != 'y':
            return 99


def check_num(num):
    if num.isdigit() == True and int(num) < 20:
            return True
    else:
        return False

while True:    
    num = input('Сколько паролей необходимо? (Максимально - 20):')
    num2 = check_num(num)
    if num2 == True:
        break
while len(longlst) != int(num):
    for i in range(1,int(num)+1):
        long = input(f'Какая длинна пароля № {i}: ')
        long2 = check_num(long)
        if long2 == True:
            longlst.append(long)
    if len(longlst) == num:
        break


def generat(usl1,usl2,usl3,usl4):
    buffer = ''
    for i in range(len(longlst)):
        for j in range(int(longlst[i])+1):
            if usl1 == True:
                buffer += choice(digits)
            if usl2 == True:
                buffer += choice(lowercase_letters)
            if usl3 == True:
                buffer += choice(uppercase_letters)
            if usl4 == True:
                buffer += choice(punctuation)
            if j == int(longlst[i]):
                choc = ''
                for _ in range(int(longlst[i])):
                    choc += choice(buffer)
                global go_psw
                go_psw.append(choc)
                if i == len(longlst)-1:
                    for num in range(len(longlst)):
                        print(num+1,'пароль:', go_psw[num])
                        global stop
                        stop = 0
                        


def answer(dig,low,upp,pun):
    while stop == 1:
        if upp == 2:
            break
        if dig == 0 and stop != 0:
            dig = input('Включать цифры? y/n: ').lower()
            a = 1
            dig = check(dig,a)
            if dig == 99:
                if stop != 0:
                    while dig == 99:
                        print('Ввели не правильные данные')
                        dig = input('Включать цифры? y/n: ').lower()
                        a = 1
                        dig = check(dig,a)

        if low == 0 and stop != 0:
            low = input('Включать маленькие буквы? y/n: ').lower()
            a = 2
            low = check(low,a)
            if low == 99:
                if stop != 0:
                    while low == 99:
                        print('Ввели не правильные данные')
                        low = input('Включать маленькие буквы? y/n: ').lower()
                        a = 2
                        low = check(low,a)
        if upp == 0 and stop != 0:
            upp = input('Включать заглавные буквы? y/n: ').lower()
            a = 3
            upp = check(upp,a)
            if upp == 99:
                if stop != 0:
                    while upp == 99:
                        print('Ввели не правильные данные')
                        upp = input('Включать заглавные буквы? y/n: ').lower()
                        a = 3
                        upp = check(upp,a)
        if pun == 0 and stop != 0:
            pun = input('Включать символы ? y/n: ').lower()
            a = 4
            pun = check(pun,a)
            if pun == 99:
                if stop != 0:
                    while pun == 99:
                        print('Ввели не правильные данные')
                        pun = input('Включать символы? y/n: ').lower()
                        a = 4
                        pun = check(pun,a)
        if a == 4:
            return generat(dig,low,upp,pun)

answer(0,0,0,0)