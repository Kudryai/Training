from datetime import timedelta,datetime,date

dates = datetime.strptime('20.12.2021', '%d.%m.%Y')

for i in range(10):
    if i == 0:
        print(dates.date().strftime('%d.%m.%Y'))
        continue
    dates += timedelta(days=i+1)
    print(dates.date().strftime('%d.%m.%Y'))