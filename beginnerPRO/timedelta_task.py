from datetime import date, timedelta, datetime

dates = input().split()
result = []

for i in range(1,len(dates)):
    try:
        res = datetime.strptime(dates[i], '%d.%m.%Y')
        res2 = datetime.strptime(dates[i-1],'%d.%m.%Y')
        ara = res-res2
        result.append(abs(ara.days))
    except:
        print(result)
print(result)