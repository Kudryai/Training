quant = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(quant):
    coord = 0
    coord = input().split()
    if int(coord[0]) > 0 and int(coord[1]) > 0: #1 плоскость
      count1 += 1
    if int(coord[0]) < 0 and int(coord[1]) > 0: #2 плоскость
      count2 += 1
    if int(coord[0]) < 0 and int(coord[1]) < 0: #3 плоскость
      count3 += 1
    if int(coord[0]) > 0 and int(coord[1]) < 0: #4 плоскость
      count4 += 1
print('Первая четверть:',count1)
print('Вторая четверть:',count2)
print('Третья четверть:',count3)
print('Четвертая четверть:',count4)