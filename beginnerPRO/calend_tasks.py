from datetime import datetime, date
import calendar 


def get_days_in_month(year, month):
    dates = datetime.strptime(f'{year} {month}', '%Y %B')
    rang = calendar.monthrange(2022, 1)
    result = []
    for i in range(1,rang[1]+1):
        result.append(date(dates.year, dates.month, i))
    return result

