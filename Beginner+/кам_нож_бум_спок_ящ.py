stady = ['ножницы', "бумага", "камень", "ящерица", "Спок",
         "ножницы", "бумага", "камень", "ящерица", "Спок"]
ans1, ans2 = input(), input()
if ans1 == ans2:
    print('ничья')
elif ans2 == stady[stady.index(ans1) - 2] or ans2 == stady[stady.index(ans1) + 1]:
    print('Тимур')
else:
    print('Руслан')
