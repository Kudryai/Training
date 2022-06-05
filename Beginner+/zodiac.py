n = int(input())
zodiac_list = ['Дракон','Змея','Лошадь','Овца','Обезьяна','Петух','Собака','Свинья',
'Крыса','Бык','Тигр','Заяц'] # China Year 0-12.
while True:
    if n > 2011:
        n -= 12
    if n < 2000:
        n += 12
    else:
        if n == 2000:
            print(zodiac_list[0])
            break
        if n == 2001:
            print(zodiac_list[1])
            break
        if n == 2002:
            print(zodiac_list[2])
            break
        if n == 2003:
            print(zodiac_list[3])
            break
        if n == 2004:
            print(zodiac_list[4])
            break
        if n == 2005:
            print(zodiac_list[5])
            break
        if n == 2006:
            print(zodiac_list[6])
            break
        if n == 2007:
            print(zodiac_list[7])
            break
        if n == 2008:
            print(zodiac_list[8])
            break
        if n == 2009:
            print(zodiac_list[9])
            break
        if n == 2010:
            print(zodiac_list[10])
            break
        if n == 2011:
            print(zodiac_list[11])
            break