num = int(input())
sum = 0
listcount = []
list = []
for i in range(num):
    list.append(input().split())
    for j in range(num):
        count = 0
        sum += int(list[i][j])
        average = int(sum)/num
    for row in list[i]:
            if int(row) > average:
                count += 1
    sum = 0
    listcount.append(count)
for coun in listcount:
    print(coun)