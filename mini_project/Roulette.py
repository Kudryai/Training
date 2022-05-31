from random import randint
print('Добро пожаловать в числовую угадайку!')
game = 1
stop = 1
count = 0
stop2 = 1
num = randint(1,100)
 
 
def is_valid(str,n):
    if n.isdigit() == True:
        if str.isdigit() == True:
            if 0 < int(str) <= int(n):
                return True
    else:
        return False


def restart(otvet):
    if yn == 'y':
        print('Поехали')
        return gameRoulette(1,0,randint(1,100))
    if yn != 'y':
        if yn != 'n':
            global stop2
            stop2 = 0
            print('Пока!Недопустимая команда')
    if yn == 'n':
        print('Пока Пока')
        global stop
        stop = 0

 
def check_num(otvet,count,num):
    if otvet > num:
        print('Введенное вами число больше загаданного')
    if otvet < num:
        print('Введенное число меньше загаданного')
    if otvet == num:
        print('Угадали!!! Поздравляем!!!', 'Попыток:',count)
        print('Спасибо что играли в угадайку от Алексея Кудрявцева')
        global yn
        yn = input('Давай еще разок? y/n:').lower()
        restart(yn)

 
def gameRoulette(game,count,num):
    count = 0
    n = input('Введи диапазон поиска числа, с которым справишься:')
    if is_valid(n,n) == True:
        num = randint(1,int(n))
    else:
        print('Диапазон только в цифрах! Пробуй еще раз')
        return gameRoulette(game,count,num)
    while game == stop and game == stop2:
        if game == 1:
            txt = input(f'Введи число от 1 до {n}:')
            count += 1
        if game == 0:
            print('Пока, Пока!!!')
            break
        if is_valid(txt,n) == True:
            check_num(int(txt),count,num)
            continue
        else:
            print(f'Давай введем все таки цифры от 1 до {n}!!')
            continue
 
 
gameRoulette(game,count,num)