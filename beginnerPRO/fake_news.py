from datetime import datetime, timedelta

time_courses = datetime.strptime('08.11.2022 12:00','%d.%m.%Y %H:%M')
time_today = datetime.strptime(input(), '%d.%m.%Y %H:%M')
time_out = time_courses - time_today


def choose_plural(amount, declensions):
    amount = str(amount)
    try:
        if int(amount[-1]) == 1 and int(amount[0]) != 1: # 1 - 10
            return f'{declensions[0]}'
        if int(amount[-1]) == 1 and len(amount) == 1: # 1 - 10
            return f'{declensions[0]}'
        if 20 >= int(amount[len(amount)-2:]) >= 10 or 9 >= int(amount[len(amount)-1:]) >= 5 or int(amount[len(amount)-1:]) == 0: # 5 - 20
            return f'{declensions[2]}'
        if 5 > int(amount[-1]) > 1: #1 - 5
            return f'{declensions[1]}'
    except:
        return -1
        
hours = time_out.seconds//3600
hours_name = choose_plural(hours, ('час','часа','часов'))
minutes = (time_out.seconds - (time_out.seconds//3600)*3600)//60
minutes_name = choose_plural(minutes, ('минута','минуты','минут'))
days = time_out.days
days_name = choose_plural(days, ('день','дня','дней'))

if days > 0 and hours > 0:
    print(f'До выхода курса осталось: {days} {days_name} и {hours} {hours_name}')
if days > 0 and hours == 0:
    print(f'До выхода курса осталось: {days} {days_name}')
if days == 0 and hours > 0 and minutes > 0:
    print(f'До выхода курса осталось: {time_out.seconds//3600} {hours_name} и {(time_out.seconds - (time_out.seconds//3600)*3600)//60} {minutes_name}')
if days == 0 and hours == 0 and minutes > 0:
    print(f'До выхода курса осталось: {minutes} {minutes_name}')
if days == 0 and hours > 0 and minutes == 0:
    print(f'До выхода курса осталось: {hours} {hours_name}')
if time_courses <= time_today:
    print('Курс уже вышел!')