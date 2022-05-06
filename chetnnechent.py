i = int(input())
i1 = i//1000
i2 = (i%1000)//100
i3 = (i%100)//10
i4 = i%10
if i1+i4 == i2-i3:
    print('ДА')
else:
    print('НЕТ')