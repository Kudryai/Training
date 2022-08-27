from datetime import datetime, date

def is_available_date(dates, some_date): 
    some_data_list = []
    result = []
    if len(some_date) > 11:
        some_aga = datetime.strptime(some_date[10:], '-%d.%m.%Y')
        some_aga1 = datetime.strptime(some_date[:10], '%d.%m.%Y')
        st = some_aga.date().toordinal()
        stop = some_aga1.date().toordinal()
        for j in range(stop, st+1):
            some_data_list.append(date.fromordinal(j))
    else:
        some_data = datetime.strptime(some_date,'%d.%m.%Y').date()
        some_data_list.append(some_data)
    for dat in dates:
        if len(dat) > 11:
            aga = datetime.strptime(dat[10:], '-%d.%m.%Y')
            aga1 = datetime.strptime(dat[:10], '%d.%m.%Y')
            n = aga.date().toordinal()
            m = aga1.date().toordinal()
            for i in range(m,n+1):
                if date.fromordinal(i) in some_data_list:
                    result.append(False)
            result.append(True)
        elif len(dat) < 11:
            aga2 = datetime.strptime(dat, '%d.%m.%Y').date()
            if aga2 in some_data_list:
                result.append(False)
            else:
                result.append(True)
    agaz = set(result)
    agaz = list(agaz)
    if len(agaz) > 2:
        return False
    else:
        return agaz[0]

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))