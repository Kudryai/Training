from datetime import datetime, timedelta, date

def fill_up_missing_dates(dates):
    result = []
    for i in range(len(dates)):
        dates[i] = datetime.strptime(dates[i], '%d.%m.%Y')
    start = max(dates) - min(dates)
    for i in range(start.days + 1):
        result.append((min(dates) + timedelta(days=i)).strftime('%d.%m.%Y'))
    return result


dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021'] # Тестовые данные

print(fill_up_missing_dates(dates))