# В русском и английском языках есть буквы, которые выглядят одинаково. 
# Вот список английских букв "AaBCcEeHKMOoPpTXxy", а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". 
# Напишите программу, которая для трёх букв из данных списков букв определяет, русские они, 
# английские или и те и другие(смесь русских и английских букв).
result = []
for _ in range(3):
    result.append(input())
result = list(map(lambda x: 'ru' if x in 'АаВСсЕеНКМОоРрТХху' else 'en', result))
check_ru = all(map(lambda x: True if x == 'ru' else False, result))
check_en = all(map(lambda x: True if x == 'en' else False, result))
if check_ru:
    print('ru')
elif check_en:
    print('en')
else:
    print('mix')
