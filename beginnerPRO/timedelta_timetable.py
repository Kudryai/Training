from datetime import timedelta,datetime,time


def timetable(strt,stop):
    strt = datetime(2021, 1, 1, int(strt[0]), int(strt[1]), 0)
    stop = datetime(2021, 1, 1, int(stop[0]), int(stop[1]), 0)
    res = strt
    result_list = []
    while res + timedelta(minutes=45) <= stop:
        nachs = (res + timedelta(minutes=45)).strftime('%H:%M')
        bams = res.strftime('%H:%M')
        result_list.append(f'{bams} - {nachs}')
        res += timedelta(minutes=55)
    return print_all(result_list)

def print_all(data):
    if len(data) > 0:
        for dates in data:
            print(dates)

start = '10:00'.split(':')
stop = '10:45'.split(':')

timetable(start, stop)