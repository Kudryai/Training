from datetime import datetime
import calendar 

ye, mo = map(int, input().split())
print(calendar.monthrange(ye, mo)[1])
