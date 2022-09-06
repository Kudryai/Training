from datetime import date, timedelta

def num_of_sundays(year): # Подсчет воскресений в году
  count = 0
  ark = date(int(year),1,1)
  for i in range(366):
    if ark.weekday() == 6 and ark.year == year:
        print(ark)
        count+=1
    ark += timedelta(days=1)
  return count

print(num_of_sundays(2000))