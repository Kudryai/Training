from datetime import datetime, date, timedelta
import calendar 


def get_all_mondays(year):
    result = []
    date = datetime(year, 1, 1)
    for i in range(366):
        if date.year != year+1:
            if calendar.weekday(date.year, date.month, date.day) == 0:
                result.append(datetime.date(date))
        date += timedelta(days=1)
    return result



print(get_all_mondays(1353))