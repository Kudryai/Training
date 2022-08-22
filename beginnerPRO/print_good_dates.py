from datetime import date

def print_good_dates(dates):
    funny_date = []
    for dt in dates:
        if dt.year == 1992 and 29 == (dt.day + dt.month):
            funny_date.append(dt)
    funny_date.sort()
    for fun in funny_date:
        print(fun.strftime('%B %d, %Y'), sep = '\n')

dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
print_good_dates(dates)