from datetime import datetime, timedelta, date

dates = datetime.strptime(input(), '%d.%m.%Y %H:%M')

open = dates.replace(hour=9, minute=0)
close = dates.replace(hour=21, minute=0)

if dates.weekday() < 5:
    result = close - dates
    if open <= dates < close:
        print(int(result.seconds/60))
    else:
        print('Магазин не работает')
else:
    open = dates.replace(hour=10, minute=0)
    close = dates.replace(hour=18, minute=0)
    result = close - dates
    if open <= dates < close:
        print(int(result.seconds/60))
    else:
        print('Магазин не работает')