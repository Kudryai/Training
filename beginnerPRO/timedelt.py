from datetime import datetime,timedelta

date_today = datetime.strptime(input(),'%d.%m.%Y')
n = int(input())
name = []
res = {}

for i in range(n):
    name.append(input().split())
    name[i][2] = datetime.strptime(name[i][2], '%d.%m.%Y')
for j in range(len(name)):
    for k in range(8):
        if name[j][2].day == (date_today + timedelta(days=k)).day and name[j][2].month == (date_today + timedelta(days=k)).month:
            res[name[j][2]] = res.get(name[j][2], ' '.join(name[j][:2]))
res = sorted(res.items())
if len(res) == 0:
    print('Дни рождения не планируются')
else:
    print(res[0][2])
