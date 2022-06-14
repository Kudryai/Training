rus = input()
ego = input()
if rus == 'ножницы' and ego == 'бумага':
    print('Тимур')
elif rus == 'камень' and ego == 'ножницы':
    print('Тимур')
elif rus == 'камень' and ego == 'ящерица':
    print('Тимур')
elif rus == 'бумага' and ego == 'камень':
    print('Тимур')
elif rus == 'бумага' and ego == 'Спок':
    print('Тимур')
elif rus == 'Спок' and ego == 'ножницы':
    print('Тимур')
elif rus == 'Спок' and ego == 'камень':
    print('Тимур')
elif rus == 'ящерица' and ego == 'Спок':
    print('Тимур')
elif rus == 'ящерица' and ego == 'бумага':
    print('Тимур')
elif rus == 'ножницы' and ego == 'ящерица':
    print('Тимур')
elif rus == ego:
    print('Ничья')
else:
    print('Руслан')