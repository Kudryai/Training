from datetime import datetime,timedelta

start = datetime.strptime(input(),'%d.%m.%Y')
stop = datetime.strptime(input(),'%d.%m.%Y')
result = []
ok = ''
while ok != 'ok':
    if (start.day + start.month) % 2 != 0:
        start = start
        ok = 'ok'
    else:
        start = start + timedelta(days=1)
start = start.toordinal()
stop = stop.toordinal()
for i in range(start,stop+1,3):
    if datetime.fromordinal(i).weekday() != 0 and datetime.fromordinal(i).weekday() != 3:
        result.append(datetime.fromordinal(i).strftime('%d.%m.%Y'))
print(*result, sep = '\n')