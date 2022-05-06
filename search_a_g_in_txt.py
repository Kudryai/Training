n = input()
total1 = 0
total2 = 0
for i in range(len(n)):
    if n[i] in "аАуУоОыЫиИэЭяЯюЮёЁеЕ":
        total1 += 1
    if n[i] in "бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩ":
        total2 += 1
print('Количество гласных букв равно', total1)
print('Количество согласных букв равно', total2)