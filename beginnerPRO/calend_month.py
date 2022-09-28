import calendar


year_month = input().split()
month = list(calendar.month_abbr)
result = {}
for i in range(1,13):
    result[month[i]] = result.get(month[i], i)
print(calendar.month(int(year_month[0]), result[year_month[1]]))
